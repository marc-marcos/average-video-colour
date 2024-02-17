import cv2
import os

def split_video(file_name):
    file_name_without_extension = file_name.split(".")[0]

    vidcap = cv2.VideoCapture('src/Test.mp4')
    success,image = vidcap.read()
    count = 0
    os.mkdir(f"temp/{file_name_without_extension}")

    while success:
        cv2.imwrite(f"temp/{file_name_without_extension}/frame{count}.jpg", image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1