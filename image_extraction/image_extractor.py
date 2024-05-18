import cv2
import input
from opencv_click import OpencvClick
import os

if __name__ == "__main__":
    img_path, output_path, result_width, result_height = input.get_input_data()

    try:
        result_width = int(result_width)
        result_height = int(result_height)
    except:
        print('\nwidth and height have to be integers!')
        print('<file> -image_path -ouput_path -width -height\n')
        os._exit(0)

    window_name = img_path
    img = cv2.imread(img_path)

    try:
        height, width, _ = img.shape
    except:
        print('\nImage not found: Did you enter the correct path and name for your image?\n')
        os._exit(0)

    # add the corner points bottom_left, bottom_right, top_left and top_rigth
    points = [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]]

    # init opnecv handler
    opencv_click = OpencvClick(
        img,
        points,
        window_name,
        width,
        height,
        result_width,
        result_height,
        output_path
    )

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, opencv_click.mouse_callback)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
