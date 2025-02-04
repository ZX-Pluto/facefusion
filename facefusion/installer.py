<<<<<<< HEAD
from typing import Dict, Tuple
import sys
import os
import tempfile
import subprocess
import inquirer
from argparse import ArgumentParser, HelpFormatter
=======
import os
import shutil
import signal
import subprocess
import sys
import tempfile
from argparse import ArgumentParser, HelpFormatter
from typing import Dict, Tuple
>>>>>>> origin/master

from facefusion import metadata, wording
from facefusion.common_helper import is_linux, is_macos, is_windows

<<<<<<< HEAD
if is_macos():
	os.environ['SYSTEM_VERSION_COMPAT'] = '0'

ONNXRUNTIMES : Dict[str, Tuple[str, str]] = {}

if is_macos():
	ONNXRUNTIMES['default'] = ('onnxruntime', '1.17.3')
else:
	ONNXRUNTIMES['default'] = ('onnxruntime', '1.17.3')
	ONNXRUNTIMES['cuda-12.2'] = ('onnxruntime-gpu', '1.17.1')
	ONNXRUNTIMES['cuda-11.8'] = ('onnxruntime-gpu', '1.17.1')
	ONNXRUNTIMES['openvino'] = ('onnxruntime-openvino', '1.15.0')
if is_linux():
	ONNXRUNTIMES['rocm-5.4.2'] = ('onnxruntime-rocm', '1.16.3')
	ONNXRUNTIMES['rocm-5.6'] = ('onnxruntime-rocm', '1.16.3')
=======
ONNXRUNTIMES : Dict[str, Tuple[str, str]] = {}

if is_macos():
	ONNXRUNTIMES['default'] = ('onnxruntime', '1.20.1')
else:
	ONNXRUNTIMES['default'] = ('onnxruntime', '1.20.1')
	ONNXRUNTIMES['cuda'] = ('onnxruntime-gpu', '1.20.1')
	ONNXRUNTIMES['openvino'] = ('onnxruntime-openvino', '1.20.0')
if is_linux():
	ONNXRUNTIMES['rocm'] = ('onnxruntime-rocm', '1.19.0')
>>>>>>> origin/master
if is_windows():
	ONNXRUNTIMES['directml'] = ('onnxruntime-directml', '1.17.3')


def cli() -> None:
<<<<<<< HEAD
	program = ArgumentParser(formatter_class = lambda prog: HelpFormatter(prog, max_help_position = 200))
	program.add_argument('--onnxruntime', help = wording.get('help.install_dependency').format(dependency = 'onnxruntime'), choices = ONNXRUNTIMES.keys())
=======
	signal.signal(signal.SIGINT, lambda signal_number, frame: sys.exit(0))
	program = ArgumentParser(formatter_class = lambda prog: HelpFormatter(prog, max_help_position = 50))
	program.add_argument('--onnxruntime', help = wording.get('help.install_dependency').format(dependency = 'onnxruntime'), choices = ONNXRUNTIMES.keys(), required = True)
>>>>>>> origin/master
	program.add_argument('--skip-conda', help = wording.get('help.skip_conda'), action = 'store_true')
	program.add_argument('-v', '--version', version = metadata.get('name') + ' ' + metadata.get('version'), action = 'version')
	run(program)


def run(program : ArgumentParser) -> None:
	args = program.parse_args()
<<<<<<< HEAD
	python_id = 'cp' + str(sys.version_info.major) + str(sys.version_info.minor)

	if not args.skip_conda and 'CONDA_PREFIX' not in os.environ:
		sys.stdout.write(wording.get('conda_not_activated') + os.linesep)
		sys.exit(1)
	if args.onnxruntime:
		answers =\
		{
			'onnxruntime': args.onnxruntime
		}
	else:
		answers = inquirer.prompt(
		[
			inquirer.List('onnxruntime', message = wording.get('help.install_dependency').format(dependency = 'onnxruntime'), choices = list(ONNXRUNTIMES.keys()))
		])
	if answers:
		onnxruntime = answers['onnxruntime']
		onnxruntime_name, onnxruntime_version = ONNXRUNTIMES[onnxruntime]

		subprocess.call([ 'pip', 'install', '-r', 'requirements.txt', '--force-reinstall' ])
		if onnxruntime == 'rocm-5.4.2' or onnxruntime == 'rocm-5.6':
			if python_id in [ 'cp39', 'cp310', 'cp311' ]:
				rocm_version = onnxruntime.replace('-', '')
				rocm_version = rocm_version.replace('.', '')
				wheel_name = 'onnxruntime_training-' + onnxruntime_version + '+' + rocm_version + '-' + python_id + '-' + python_id + '-manylinux_2_17_x86_64.manylinux2014_x86_64.whl'
				wheel_path = os.path.join(tempfile.gettempdir(), wheel_name)
				wheel_url = 'https://download.onnxruntime.ai/' + wheel_name
				subprocess.call([ 'curl', '--silent', '--location', '--continue-at', '-', '--output', wheel_path, wheel_url ])
				subprocess.call([ 'pip', 'uninstall', wheel_path, '-y', '-q' ])
				subprocess.call([ 'pip', 'install', wheel_path, '--force-reinstall' ])
				os.remove(wheel_path)
		else:
			subprocess.call([ 'pip', 'uninstall', 'onnxruntime', onnxruntime_name, '-y', '-q' ])
			if onnxruntime == 'cuda-12.2':
				subprocess.call([ 'pip', 'install', onnxruntime_name + '==' + onnxruntime_version, '--extra-index-url', 'https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple', '--force-reinstall' ])
			else:
				subprocess.call([ 'pip', 'install', onnxruntime_name + '==' + onnxruntime_version, '--force-reinstall' ])
=======
	has_conda = 'CONDA_PREFIX' in os.environ
	onnxruntime_name, onnxruntime_version = ONNXRUNTIMES.get(args.onnxruntime)

	if not args.skip_conda and not has_conda:
		sys.stdout.write(wording.get('conda_not_activated') + os.linesep)
		sys.exit(1)

	subprocess.call([ shutil.which('pip'), 'install', '-r', 'requirements.txt', '--force-reinstall' ])

	if args.onnxruntime == 'rocm':
		python_id = 'cp' + str(sys.version_info.major) + str(sys.version_info.minor)

		if python_id in [ 'cp310', 'cp312' ]:
			wheel_name = 'onnxruntime_rocm-' + onnxruntime_version + '-' + python_id + '-' + python_id + '-linux_x86_64.whl'
			wheel_path = os.path.join(tempfile.gettempdir(), wheel_name)
			wheel_url = 'https://repo.radeon.com/rocm/manylinux/rocm-rel-6.3.1/' + wheel_name
			subprocess.call([ shutil.which('curl'), '--silent', '--location', '--continue-at', '-', '--output', wheel_path, wheel_url ])
			subprocess.call([ shutil.which('pip'), 'uninstall', 'onnxruntime', wheel_path, '-y', '-q' ])
			subprocess.call([ shutil.which('pip'), 'install', wheel_path, '--force-reinstall' ])
			os.remove(wheel_path)
	else:
		subprocess.call([ shutil.which('pip'), 'uninstall', 'onnxruntime', onnxruntime_name, '-y', '-q' ])
		subprocess.call([ shutil.which('pip'), 'install', onnxruntime_name + '==' + onnxruntime_version, '--force-reinstall' ])

	if args.onnxruntime == 'cuda' and has_conda:
		library_paths = []

		if is_linux():
			if os.getenv('LD_LIBRARY_PATH'):
				library_paths = os.getenv('LD_LIBRARY_PATH').split(os.pathsep)

			python_id = 'python' + str(sys.version_info.major) + '.' + str(sys.version_info.minor)
			library_paths.extend(
			[
				os.path.join(os.getenv('CONDA_PREFIX'), 'lib'),
				os.path.join(os.getenv('CONDA_PREFIX'), 'lib', python_id, 'site-packages', 'tensorrt_libs')
			])
			library_paths = list(dict.fromkeys([ library_path for library_path in library_paths if os.path.exists(library_path) ]))

			subprocess.call([ shutil.which('conda'), 'env', 'config', 'vars', 'set', 'LD_LIBRARY_PATH=' + os.pathsep.join(library_paths) ])

		if is_windows():
			if os.getenv('PATH'):
				library_paths = os.getenv('PATH').split(os.pathsep)

			library_paths.extend(
			[
				os.path.join(os.getenv('CONDA_PREFIX'), 'Lib'),
				os.path.join(os.getenv('CONDA_PREFIX'), 'Lib', 'site-packages', 'tensorrt_libs')
			])
			library_paths = list(dict.fromkeys([ library_path for library_path in library_paths if os.path.exists(library_path) ]))

			subprocess.call([ shutil.which('conda'), 'env', 'config', 'vars', 'set', 'PATH=' + os.pathsep.join(library_paths) ])

	if args.onnxruntime in [ 'directml', 'rocm' ]:
		subprocess.call([ shutil.which('pip'), 'install', 'numpy==1.26.4', '--force-reinstall' ])
>>>>>>> origin/master
