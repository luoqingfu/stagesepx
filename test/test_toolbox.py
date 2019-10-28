import os

from stagesepx import toolbox

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGE_NAME = "demo.jpg"
IMAGE_PATH = os.path.join(PROJECT_PATH, IMAGE_NAME)
VIDEO_NAME = "demo.mp4"
VIDEO_PATH = os.path.join(PROJECT_PATH, VIDEO_NAME)
assert os.path.isfile(IMAGE_PATH), f"{IMAGE_NAME} not existed!"
assert os.path.isfile(VIDEO_PATH), f"{VIDEO_PATH} not existed!"


def test_turn_blur():
    image = toolbox.imread(IMAGE_PATH)
    grey = toolbox.turn_grey(image)
    toolbox.turn_blur(grey)


def test_turn_grey():
    image = toolbox.imread(IMAGE_PATH)
    toolbox.turn_grey(image)


def test_turn_binary():
    image = toolbox.imread(IMAGE_PATH)
    toolbox.turn_binary(image)


def test_turn_surf_desc():
    image = toolbox.imread(IMAGE_PATH)
    toolbox.turn_surf_desc(image)


def test_turn_lbp_desc():
    image = toolbox.imread(IMAGE_PATH)
    toolbox.turn_lbp_desc(image)


def test_get_frame():
    with toolbox.video_capture(VIDEO_PATH) as cap:
        first = 5
        second = 8

        actual = toolbox.get_frame_time(cap, first)
        should = toolbox.get_current_frame_time(cap)
        # should be frame 5
        assert actual == should

        # 5 -> 8 -> 5
        frame = toolbox.get_frame(cap, second, True)
        assert frame is not None
        assert toolbox.get_current_frame_id(cap) == first

        # 5 -> 8
        frame = toolbox.get_frame(cap, second)
        assert frame is not None
        assert toolbox.get_current_frame_id(cap) == second
