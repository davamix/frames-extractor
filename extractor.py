# coding=utf-8

# https://stackoverflow.com/a/33399711/844372

# Usage:

# To extract frames: 
# python extractor.py --frames 10 video_file.mp4

# To show information: 
# python extractor.py --info video_file.mp4

import cv2
import argparse
import os
import sys
from tqdm import tqdm

# Return the total frames in the video
def get_frames_video(video):
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    return total_frames

# Show basic information about the video
def show_info_video(video):
    print("Frames: {}".format(get_frames_video(video)))
    print("Frame rate: {}".format(video.get(cv2.CAP_PROP_FPS)))
    print("Height: {}".format(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("Width: {}".format(video.get(cv2.CAP_PROP_FRAME_WIDTH)))

# Arguments builder
parser = argparse.ArgumentParser()
parser.add_argument('file', help='Video file')
parser.add_argument('--frames', '-f', help='Percentage of total frames to extract (int)', type=int)
parser.add_argument('--info', '-i', dest='info', action='store_true', help='Show information about the video (do not extract anything)')
parser.set_defaults(info=False)

args = parser.parse_args()
video_file = args.file
frames_to_extract = args.frames if args.frames else 0

if not os.path.isfile(video_file):
    print("File '{}' does not exists".format(video_file))
    sys.exit()

# Open the video    
video = cv2.VideoCapture(video_file)

# Read the 1st frame 
success, image = video.read()

current_frame = 0
total_frames_captured = 0

if success:
    if args.info:
        show_info_video(video)
        sys.exit()

    # Get the total frames in the video
    total_frames = get_frames_video(video)
    
    frames_to_skip = 0
    if frames_to_extract > 0:
        frames_to_skip = total_frames / (total_frames * frames_to_extract / 100)

    skipped_frame = 0

    # Progress bar
    for i in tqdm(range(total_frames)):
        # If you don't want to use the progress bar, remove the "for" above
        # and change this "if..else" by a "while success"
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