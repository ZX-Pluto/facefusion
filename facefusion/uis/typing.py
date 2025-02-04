<<<<<<< HEAD
from typing import Literal, Any, IO
import gradio

File = IO[Any]
Component = gradio.File or gradio.Image or gradio.Video or gradio.Slider
ComponentName = Literal\
[
=======
from typing import Any, Dict, IO, Literal

File = IO[Any]
Component = Any
ComponentOptions = Dict[str, Any]
ComponentName = Literal\
[
	'age_modifier_direction_slider',
	'age_modifier_model_dropdown',
	'benchmark_cycles_slider',
	'benchmark_runs_checkbox_group',
	'deep_swapper_model_dropdown',
	'deep_swapper_morph_slider',
	'expression_restorer_factor_slider',
	'expression_restorer_model_dropdown',
	'face_debugger_items_checkbox_group',
	'face_detector_angles_checkbox_group',
	'face_detector_model_dropdown',
	'face_detector_score_slider',
	'face_detector_size_dropdown',
	'face_editor_eyebrow_direction_slider',
	'face_editor_eye_gaze_horizontal_slider',
	'face_editor_eye_gaze_vertical_slider',
	'face_editor_eye_open_ratio_slider',
	'face_editor_head_pitch_slider',
	'face_editor_head_roll_slider',
	'face_editor_head_yaw_slider',
	'face_editor_lip_open_ratio_slider',
	'face_editor_model_dropdown',
	'face_editor_mouth_grim_slider',
	'face_editor_mouth_position_horizontal_slider',
	'face_editor_mouth_position_vertical_slider',
	'face_editor_mouth_pout_slider',
	'face_editor_mouth_purse_slider',
	'face_editor_mouth_smile_slider',
	'face_enhancer_blend_slider',
	'face_enhancer_model_dropdown',
	'face_enhancer_weight_slider',
	'face_landmarker_model_dropdown',
	'face_landmarker_score_slider',
	'face_mask_blur_slider',
	'face_mask_padding_bottom_slider',
	'face_mask_padding_left_slider',
	'face_mask_padding_right_slider',
	'face_mask_padding_top_slider',
	'face_mask_regions_checkbox_group',
	'face_mask_types_checkbox_group',
	'face_selector_age_range_slider',
	'face_selector_gender_dropdown',
	'face_selector_mode_dropdown',
	'face_selector_order_dropdown',
	'face_selector_race_dropdown',
	'face_swapper_model_dropdown',
	'face_swapper_pixel_boost_dropdown',
	'face_occluder_model_dropdown',
	'face_parser_model_dropdown',
	'frame_colorizer_blend_slider',
	'frame_colorizer_model_dropdown',
	'frame_colorizer_size_dropdown',
	'frame_enhancer_blend_slider',
	'frame_enhancer_model_dropdown',
	'job_list_job_status_checkbox_group',
	'lip_syncer_model_dropdown',
	'output_image',
	'output_video',
	'output_video_fps_slider',
	'preview_frame_slider',
	'processors_checkbox_group',
	'reference_face_distance_slider',
	'reference_face_position_gallery',
>>>>>>> origin/master
	'source_audio',
	'source_image',
	'target_image',
	'target_video',
<<<<<<< HEAD
	'preview_frame_slider',
	'trim_frame_start_slider',
	'trim_frame_end_slider',
	'face_selector_mode_dropdown',
	'reference_face_position_gallery',
	'reference_face_distance_slider',
	'face_analyser_order_dropdown',
	'face_analyser_age_dropdown',
	'face_analyser_gender_dropdown',
	'face_detector_model_dropdown',
	'face_detector_size_dropdown',
	'face_detector_score_slider',
	'face_landmarker_score_slider',
	'face_mask_types_checkbox_group',
	'face_mask_blur_slider',
	'face_mask_padding_top_slider',
	'face_mask_padding_bottom_slider',
	'face_mask_padding_left_slider',
	'face_mask_padding_right_slider',
	'face_mask_region_checkbox_group',
	'frame_processors_checkbox_group',
	'face_debugger_items_checkbox_group',
	'face_enhancer_model_dropdown',
	'face_enhancer_blend_slider',
	'face_swapper_model_dropdown',
	'frame_colorizer_model_dropdown',
	'frame_colorizer_blend_slider',
	'frame_colorizer_size_dropdown',
	'frame_enhancer_model_dropdown',
	'frame_enhancer_blend_slider',
	'lip_syncer_model_dropdown',
	'output_path_textbox',
	'output_video_fps_slider',
	'benchmark_runs_checkbox_group',
	'benchmark_cycles_slider',
	'webcam_mode_radio',
	'webcam_resolution_dropdown',
	'webcam_fps_slider'
]

=======
	'ui_workflow_dropdown',
	'webcam_device_id_dropdown',
	'webcam_fps_slider',
	'webcam_mode_radio',
	'webcam_resolution_dropdown'
]

JobManagerAction = Literal['job-create', 'job-submit', 'job-delete', 'job-add-step', 'job-remix-step', 'job-insert-step', 'job-remove-step']
JobRunnerAction = Literal['job-run', 'job-run-all', 'job-retry', 'job-retry-all']

>>>>>>> origin/master
WebcamMode = Literal['inline', 'udp', 'v4l2']
StreamMode = Literal['udp', 'v4l2']
