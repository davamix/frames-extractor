# https://stackoverflow.com/a/33399711/844372

# python extractor.py video_file.mp4 --frames 10

import cv2
import argparse
import os
from tqdm import tqdm

# Arguments builder
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Video file")
parser.add_argument("--frames", help="Percentage of total frames to extract (int)", type=int)
args = parser.parse_args()

video_file = args.file
frames_to_extract = args.frames if args.frames else 0

if not os.path.isfile(video_file):
    print("File '{}' does not exists".format(video_file))
    exit()

# Open video    
video = cv2.VideoCapture(video_file)

# Read the 1st frame 
success, image = video.read()

current_frame = 0
total_frames_captured = 0

if success:
    # Get total frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frames_to_skip = 0
    if frames_to_extract > 0:
        frames_to_skip = total_frames / (total_frames * frames_to_extract / 100)

    skipped_frame = 0

    # Progress bar
    for i in tqdm(range(total_frames)):
        if success:
            if current_frame >= skipped_frame:
                cv2.imwrite("frame%d.jpg" % current_frame, image)  # save frame as JPEG file
                skipped_frame += frames_to_skip
                
                #print("Captured frame: {}".format(count))
                total_frames_captured += 1
            
            success,image = video.read()
            current_frame += 1

        else:
            print("The end!")

    print("Total frames in video: {}".format(total_frames))
    print("Total frames captured: {}".format(total_frames_captured))
else:
    print("ERROR: Cannot open video.")