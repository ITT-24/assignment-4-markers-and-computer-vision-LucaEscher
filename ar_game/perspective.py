import cv2
import numpy as np


class Perspective:

    def __init__(self) -> None:
        pass

    # copied from aruco_sample.py
    # get four markers from paper
    def detect_markers(self, frame, detector):
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect ArUco markers in the frame
        corners, ids, rejectedImgPoints = detector.detectMarkers(gray)

        filtered_corners = []
        # Check if marker is detected
        if ids is not None:
            # Draw lines along the sides of the marker
            # aruco.drawDetectedMarkers(frame, corners)

            # filter aruco markers and draw ids through uncommenting
            for id in range(len(ids)):
                if ids[id][0] in [0, 1, 2, 3]:
                    # only keep corners which have the id in range of 0 to 3
                    c = corners[id][0]
                    filtered_corners.append(c)
                    # text_position = (int(c[0][0]), int(c[0][1]) - 10)
                    # cv2.putText(frame, str(ids[id][0]), text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

        # turn array back to (1, 4, 2) structure
        filtered_corners = [np.expand_dims(arr, axis=0) for arr in filtered_corners]
        return frame, filtered_corners

    # google search:
    # order coordinate points clockwise with opencv and python
    # code copied from https://gist.github.com/flashlib/e8261539915426866ae910d55a3f9959 (with slight adjustments)
    def order_points_clockwise(self, pts):
        if not isinstance(pts, np.ndarray):
            raise ValueError("Input pts must be a numpy array")
        if pts.ndim != 2 or pts.shape[1] != 2:
            raise ValueError("Input pts must be a 2D array with shape (N, 2)")

        xSorted = pts[np.argsort(pts[:, 0]), :]
        # grab the left-most and right-most points from the sorted
        # x-roodinate points
        leftMost = xSorted[:2, :]
        rightMost = xSorted[2:, :]

        # now, sort the left-most coordinates according to their
        # y-coordinates so we can grab the top-left and bottom-left
        # points, respectively
        leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
        (tl, bl) = leftMost

        # if use Euclidean distance, it will run in error when the object
        # is trapezoid. So we should use the same simple y-coordinates order method.

        # now, sort the right-most coordinates according to their
        # y-coordinates so we can grab the top-right and bottom-right
        # points, respectively
        rightMost = rightMost[np.argsort(rightMost[:, 1]), :]
        (tr, br) = rightMost

        # return the coordinates in top-left, top-right,
        # bottom-right, and bottom-left order
        return np.array([tl, tr, br, bl], dtype="float32")

    # inspired from ./image_extraction/opencv_click.py
    def transform_image(self, frame, tags):
        height, width, _ = frame.shape
        corners = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
        corner_tags = []
        index = 0
        for tag in tags:
            tag[0] = self.order_points_clockwise(tag[0])
            corner_tags.append(tag[0][index])
            index += 1
        corner_tags = np.float32(corner_tags)
        M = cv2.getPerspectiveTransform(corner_tags, corners)
        frame = cv2.warpPerspective(frame, M, (width, height))
        return frame

    # used computer_vision.ipynb as inspiration and help
    def get_finger_contour(self, frame):
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img_contours = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_contours = np.flip(img_contours, axis=0)
        return img_contours, contours
