### ---------- Handle Command Line Arguments ----------

import argparse

hide_img = False # default is to display image after predictions

a = argparse.ArgumentParser(description="Predict the class of a given driver image.")
#a.add_argument("--image", help="path to image", default="/home/saurabh/Development/TechCrunch-Berlin-2019/distracted-driver/dataset/imgs/test/img_1.jpg")
a.add_argument("--image", help="path to image", default="D:/TechCrunch/testing/projectX-master/projectX-master/distracted-driver-detection/src/video_test")
a.add_argument("--hide_img", action="store_true", help="do NOT display image on prediction termination")
args = a.parse_args()

if args.hide_img:
    hide_img = True
    
#if args.image is not None:
#    img_path = args.image
    
### ---------- Import Relevant Libraries ----------

from keras.preprocessing.image import load_img, img_to_array
from helper import create_top_model, class_labels, target_size
import numpy as np
from keras import applications
import operator
#import matplotlib.pyplot as plt
import argparse
import os
import cv2
from PIL import Image
#import requests


dir_path = args.image

mean_height = 0
mean_width = 0
num_of_images = len(os.listdir(dir_path))
for file in os.listdir(dir_path): 
    im = Image.open(os.path.join(dir_path, file)) 
    width, height = im.size 
    mean_width += width 
    mean_height += height 
mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images)



for file in os.listdir(dir_path): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
        # opening image using PIL Image 
        im = Image.open(os.path.join(dir_path, file))  
   
        # im.size includes the height and width of image 
        width, height = im.size    
        #print(width, height) 
  
        # resizing  
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
        imResize.save( file, 'JPEG', quality = 95) # setting quality 
        # printing each resized image name 
        #print(im.filename.split('\\')[-1], " is resized")  
  
  
# Video Generating function 
def generate_video(): 
    image_folder = dir_path # make sure to use your folder 
    video_name = 'mygeneratedvideo.avi'
    os.chdir("hello") 
      
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")] 
     
    # Array images should only consider 
    # the image files ignoring others if any 
    print(images)  
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, 0, 5, (width, height))  
  
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 
  
generate_video()
"""
for dirpath, dirnames, filenames in os.walk(dir_path):
    counter = 1
    for i in range(len(filenames)):
        img_path = dir_path+filenames[i]
        
        img = cv2.imread(img_path)
        cv2.imwrite("video_test/Super_Test_%d.jpg" % counter,img)
        cv2.imshow("test", img)
        counter += 1
        cv2.waitKey(1) 
    
    cv2.destroyAllWindows()
"""