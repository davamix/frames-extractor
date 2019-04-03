# Frames extractor

Script to extract a % of frames from a video and saved them as an image file.

This is useful when you want to take a lot of pictures to feed your ML model. This script combined with the [data-augmentation script](https://github.com/davamix/data-augmentation) can save your time :)

## Usage
To extract the 75% of frames:

`python extractor.py --frames 75 video_file.mp4 `

To extract all frames from the video:

`python extractor.py video_file.mp4`

To get basic information about the video:

`python extractor.py --info video_file.mp4`