import subprocess
import sys
<<<<<<< HEAD
import pytest

from facefusion.download import conditional_download
=======

import pytest

from facefusion.download import conditional_download
from facefusion.jobs.job_manager import clear_jobs, init_jobs
from .helper import get_test_example_file, get_test_examples_directory, get_test_jobs_directory, get_test_output_file, is_test_output_file, prepare_test_output_directory
>>>>>>> origin/master


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
<<<<<<< HEAD
	conditional_download('.assets/examples',
	[
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/source.jpg',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-240p.mp4'
	])
	subprocess.run([ 'ffmpeg', '-i', '.assets/examples/target-240p.mp4', '-vframes', '1', '.assets/examples/target-240p.jpg' ])


def test_enhance_frame_to_image() -> None:
	commands = [ sys.executable, 'run.py', '--frame-processors', 'frame_enhancer', '-t', '.assets/examples/target-240p.jpg', '-o', '.assets/examples/test_enhance_frame_to_image.jpg', '--headless' ]
	run = subprocess.run(commands, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

	assert run.returncode == 0
	assert 'image succeed' in run.stdout.decode()


def test_enhance_frame_to_video() -> None:
	commands = [ sys.executable, 'run.py', '--frame-processors', 'frame_enhancer', '-t', '.assets/examples/target-240p.mp4', '-o', '.assets/examples/test_enhance_frame_to_video.mp4', '--trim-frame-end', '10', '--headless' ]
	run = subprocess.run(commands, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

	assert run.returncode == 0
	assert 'video succeed' in run.stdout.decode()
=======
	conditional_download(get_test_examples_directory(),
	[
		'https://github.com/facefusion/facefusion-assets/releases/download/examples-3.0.0/source.jpg',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples-3.0.0/target-240p.mp4'
	])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vframes', '1', get_test_example_file('target-240p.jpg') ])


@pytest.fixture(scope = 'function', autouse = True)
def before_each() -> None:
	clear_jobs(get_test_jobs_directory())
	init_jobs(get_test_jobs_directory())
	prepare_test_output_directory()


def test_enhance_frame_to_image() -> None:
	commands = [ sys.executable, 'facefusion.py', 'headless-run', '--jobs-path', get_test_jobs_directory(), '--processors', 'frame_enhancer', '-t', get_test_example_file('target-240p.jpg'), '-o', get_test_output_file('test-enhance-frame-to-image.jpg') ]

	assert subprocess.run(commands).returncode == 0
	assert is_test_output_file('test-enhance-frame-to-image.jpg') is True


def test_enhance_frame_to_video() -> None:
	commands = [ sys.executable, 'facefusion.py', 'headless-run', '--jobs-path', get_test_jobs_directory(), '--processors', 'frame_enhancer', '-t', get_test_example_file('target-240p.mp4'), '-o', get_test_output_file('test-enhance-frame-to-video.mp4'), '--trim-frame-end', '1' ]

	assert subprocess.run(commands).returncode == 0
	assert is_test_output_file('test-enhance-frame-to-video.mp4') is True
>>>>>>> origin/master
