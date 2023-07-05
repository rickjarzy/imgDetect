from typing import Tuple
import numpy as np
import cv2


def buffered_bbox(input_bbox:dict, input_img_shape:Tuple[int,int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    x_min = input_bbox["xmin"]
    y_min = input_bbox["ymin"]
    x_max = input_bbox["xmax"]
    y_max = input_bbox["ymax"]

    print(f"buffered : {input_img_shape}")
    img_h = input_img_shape[0]
    img_w = input_img_shape[1]
    
    if (img_w - x_min) > 5 and (x_min-5) > 0:
        x_min = x_min - 5
    if (img_w - x_max) > 5 and (x_max+5) < img_w:
        x_max = x_max + 5
    if (img_h - y_min) > 5 and (y_min-5) > 0:
        y_min = y_min - 5
    if (img_h - y_max) > 5 and (y_max+5) < img_h:
        y_max = y_max + 5    
    print(f"buffered : {(x_min, y_min), (x_max, y_max)}")
    # add buffer 
    return (x_min, y_min), (x_max, y_max)

def show_cropped_img(input_img:np.ndarray, input_bbox_start:Tuple[int,int], input_bbox_end:Tuple[int, int]) -> None:

    bbox_color = (255,0,0)
    bbox_thickness = 2
    
    input_img = cv2.rectangle(input_img, input_bbox_start, input_bbox_end, bbox_color, bbox_thickness)
    cv2.imshow("chicken pic", input_img)

    img_roi = input_img[input_bbox_start[1]:input_bbox_end[1],input_bbox_start[0]:input_bbox_end[0],:]
    cv2.imshow("ROI", img_roi)
    cv2.waitKey(0)