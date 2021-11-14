
from typing import MutableMapping
import cv2 as cv
import cv2
import argparse
import os.path
import Integration
import detection
import multiprocessing as mp
import time

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser(description='Object Detection and Tracking using YOLO in OPENCV')
parser.add_argument('--image', help='Path to image file.')
parser.add_argument('--video', help='xtest.mp4')
parser.add_argument("-s", "--skip_frames", type=int, default=1,
    help="# of skip frames between detections")
args = parser.parse_args()

# Process inputs
winName = 'Crowd Analysis using YOLO'
#cv.namedWindow(winName, cv.WINDOW_NORMAL)

#outputFile = "yolo_out_py.avi"
if (args.image):
    # Open the image file
    if not os.path.isfile(args.image):
        print("Input image file ", args.image, " doesn't exist")
        sys.exit(1)
    cap = cv.VideoCapture(args.image)
    
elif (args.video):
    # Open the video file
    if not os.path.isfile(args.video):
        print("Input video file ", args.video, " doesn't exist")
        sys.exit(1)
    cap = cv.VideoCapture(args.video)
    #outputFile = args.video[:-4]+'_yolo_out_py.avi'
else:
    # Webcam input
    #cap = cv.VideoCapture('./test.mp4')
    res = cv.VideoCapture(0)
   
Integration.run(res,args)

   