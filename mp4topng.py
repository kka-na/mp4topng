import cv2
import sys

if len(sys.argv) != 3 :  
  print("input *.mp4 file path & save directory path")
  print("[HELP] python3 mp4topngconver.py /path/to/abcd.mp4 /path/to/save")
  sys.exit()

file_path = sys.argv[1]
save_dir = sys.argv[2]

vidcap = cv2.VideoCapture(file_path)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(str(save_dir)+"/"+"%d.png" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  count += 1