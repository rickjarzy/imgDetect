import argparse
import logging
import cv2
import os
import glob
import json
import time

from imageutils.utils import buffered_bbox, show_cropped_img

def main() -> None:

    logging.basicConfig(level=logging.INFO)
    try:    

        data_dir = r"..\\data\\chicken_rgb_data_full"
        out_dir = r"C:\\Users\\parzberg\\private\\dev\\python\\chickendetection\\data\\chicken_rgb_data_croped"

        if os.path.exists(out_dir):
            logging.info(f"Outdir - {out_dir} exists")
        else:
            logging.info(f"Outdir - {out_dir} exists not - create it ...")
            os.mkdir(out_dir)

        os.chdir(data_dir)

        full_images = glob.glob("*.jpg")
        pos_txt = glob.glob("*.txt")
        
        img_cou = 0
        num_pics = len(full_images)
        for i, img_name in enumerate(full_images):
            img_croped_name:str = os.path.join(out_dir,img_name.split(".")[0] + "croped.jpg")
            logging.info(f"\n{img_cou} of {num_pics}\ntxt: {pos_txt[i]}\nimg: {img_name}\nwrite_name: {img_croped_name}")
            bbox:dict = {}
            with open(pos_txt[i]) as bbox_file:
                bbox = dict(json.loads(bbox_file.readline()))
                logging.info(f"bbox: {bbox}")
            img = cv2.imread(img_name)
            img_shape = img.shape
            
            bbox_start, bbox_end = buffered_bbox(bbox, img_shape)


            img_roi = img[bbox_start[1]:bbox_end[1],bbox_start[0]:bbox_end[0],:]
            cv2.imwrite(img_croped_name, img_roi)
            img_cou+=1
            # if img_cou == 12:
            #     break
            # else:
            #     #show_cropped_img(img, bbox_start, bbox_end)
            #     img_cou += 1
            
        


        
        logging.info("Programm ENDE")
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        logging.info("Programm terminated by user")

if __name__ == "__main__":
    main()