import cv2
import numpy as np


class OpencvClick:

    def __init__(self, image: np.ndarray, points: list, window_name: str, img_width: int, img_height: int, result_width: int, result_height: int, output_path: str) -> None:
        self.image = image
        self.points = points
        self.window_name = window_name
        self.img_width = img_width
        self.img_height = img_height
        self.result_width = result_width
        self.result_height = result_height
        self.output_path = output_path

        # save original image for reset
        self.original_img = image.copy()

    def mouse_callback(self, event, x, y, flags, param) -> None:
        color_blue = (255, 0, 0)

        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append([x, y])
            img = cv2.circle(self.image, (x, y), 5, color_blue, -1)
            cv2.imshow(self.window_name, img)

            if len(self.points) == 8:
                # source for transform and warp perspective: https://theailearner.com/tag/cv2-getperspectivetransform/
                input_pts = self.sort_points(self.points)
                input_pts = np.float32(input_pts)
                output_pts = np.float32(self.points[:4])

                # compute perspective transoform M
                M = cv2.getPerspectiveTransform(input_pts, output_pts)
                output_img = cv2.warpPerspective(self.image, M, (self.img_width - 1, self.img_height - 1), flags=cv2.INTER_LINEAR)
                # img to result_width and result_height as specified in the skript
                img = cv2.resize(output_img, (self.result_width, self.result_height), interpolation=cv2.INTER_AREA)

                cv2.imshow(self.window_name, img)

                key = cv2.waitKey(0)
                # esc > restart
                if key == 27:
                    print('RESTART')
                    self.restart()

                # s > save file
                elif key == ord('s'):
                    print(f'Saved {self.window_name} to {self.output_path}')
                    cv2.imwrite(self.output_path, img)
                    self.restart()

    def restart(self):
        self.points = self.points[:4]
        self.image = self.original_img.copy()
        cv2.imshow(self.window_name, self.image)

    # bring the added points in the same order as the corner points
    def sort_points(self, points: list) -> list:
        pts = points[4:]
        corner_pts = points[:4]
        vectors = []
        sorted_pts = pts.copy()
        for pt in pts:
            for corner in corner_pts:
                vectors.append(self.euclidean_distance(pt[0], pt[1], corner[0], corner[1]))
            nearest_corner = corner_pts[vectors.index(np.min(vectors))]
            index = corner_pts.index(nearest_corner)
            sorted_pts[index] = pt
            vectors.clear()
        return sorted_pts

    # generated with chatgpt (see chatgpt.md) and adjusted by me
    # measure distance between two points
    def euclidean_distance(self, x1: int, y1: int, x2: int, y2: int) -> float:
        distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance


"""     # this method was used to draw lines between the points but is not needed and therefore not used 
        def draw_lines(self, points, color, thickness=2) -> None:
            for i in range(len(points)):
                start_point = points[i]
                end_point = points[(i + 1) % len(points)]
                cv2.line(self.image, start_point, end_point, color, thickness)
            cv2.imshow('Line', self.image)
 """
