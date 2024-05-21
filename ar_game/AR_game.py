from bug_smasher import BugSmasher
import config
import cv2
import numpy as np
import os
from perspective import Perspective
import pyglet
from pyglet.gl import glClearColor
from PIL import Image
import sys

# partly copied from aruco_sample.py 
video_id = 0
cam_res = True

if len(sys.argv) > 1:
    video_id = int(sys.argv[1])
if len(sys.argv) > 2:
    cam_res = sys.argv[2]

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
aruco_params = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

cap = cv2.VideoCapture(video_id)

if cam_res == 'True':
    resolution = cap.read()[1].shape
    config.HEIGHT = resolution[0]
    config.WIDTH = resolution[1]

window = pyglet.window.Window(config.WIDTH, config.HEIGHT, caption='BUG_SMASHER!')

# copied from opencv_pyglet (which i deleted then since it was not needed anymore)
# converts OpenCV image to PIL image and then to pyglet texture
# https://gist.github.com/nkymut/1cb40ea6ae4de0cf9ded7332f1ca0d55
def cv2glet(img, fmt):
    '''Assumes image is in BGR color space. Returns a pyimg object'''
    if fmt == 'GRAY':
        rows, cols = img.shape
        channels = 1
    else:
        rows, cols, channels = img.shape
    raw_img = Image.fromarray(img).tobytes()

    top_to_bottom_flag = -1
    bytes_per_row = channels*cols
    pyimg = pyglet.image.ImageData(width=cols,
                                   height=rows,
                                   fmt=fmt,
                                   data=raw_img,
                                   pitch=top_to_bottom_flag*bytes_per_row)
    return pyimg


@window.event
def on_draw():
    window.clear()
    ret, frame = cap.read()

    perspective = Perspective()
    frame, tags = perspective.detect_markers(frame, detector)

    if len(tags) == 4:
        frame = perspective.transform_image(frame, np.float32(tags))
        frame, contours = perspective.get_finger_contour(frame)
        for contour in contours:
            x = contour[0][0][0]
            y = contour[0][0][1]
            smashed_bug = bug_smasher.bugs.check_collision([x, y])
            if smashed_bug:
                bug_smasher.bugs.destroy_bug(smashed_bug)
                bug_smasher.adjust_score(smashed_bug)

    img = cv2glet(frame, 'BGR')
    img.blit(0, 0, 0)
    bug_smasher.update()


@window.event
def on_key_press(symbol, modifiers):
    # R = restart game
    if symbol == pyglet.window.key.R:
        bug_smasher.restart()

    # Q = quit game
    elif symbol == pyglet.window.key.Q:
        os._exit(0)

    # SPACE = start the game
    elif symbol == pyglet.window.key.SPACE:
        bug_smasher.bugs.start_spawner()
        bug_smasher.game_state = 1


if __name__ == '__main__':
    bug_smasher = BugSmasher(window_height=config.HEIGHT, window_width=config.WIDTH)
    bug_smasher.run()
