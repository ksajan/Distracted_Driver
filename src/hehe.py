### ---------- Handle Command Line Arguments ----------

import argparse

hide_img = False # default is to display image after predictions

a = argparse.ArgumentParser(description="Predict the class of a given driver image.")
#a.add_argument("--image", help="path to image", default="/home/saurabh/Development/TechCrunch-Berlin-2019/distracted-driver/dataset/imgs/test/img_1.jpg")
a.add_argument("--image", help="path to image", default="p015/")
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
import matplotlib.pyplot as plt
import argparse
import os
import cv2
#import requests

dir_path = args.image

for dirpath, dirnames, filenames in os.walk(dir_path):
    counter = 1
    for i in range(len(filenames)):
        img_path = dir_path+filenames[i]
        
        img = cv2.imread(img_path)
        # prepare image for classification using keras utility functions
        image = load_img(img_path, target_size=target_size)
        
        image_arr = img_to_array(image) # convert from PIL Image to NumPy array
        image_arr /= 255
    
        # to be able to pass it through the network and use batches, we want it with shape (1, 224, 224, 3)
        image_arr = np.expand_dims(image_arr, axis=0)
        # print(image.shape)

        # build the VGG16 network  
        model = applications.VGG16(include_top=False, weights='imagenet')  
    
        # get the bottleneck prediction from the pre-trained VGG16 model  
        bottleneck_features = model.predict(image_arr) 
    
        # build top model  
        model = create_top_model("softmax", bottleneck_features.shape[1:])
    
        model.load_weights("res/top_model_weights.h5")
    
        predicted = model.predict(bottleneck_features)
        decoded_predictions = dict(zip(class_labels, predicted[0]))
        decoded_predictions = sorted(decoded_predictions.items(), key=operator.itemgetter(1), reverse=True)
    
        print()
        x_coor = 5
        y_coor = 380
        count = 1

        for key, value in decoded_predictions[:5]:        
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,"{}. {}: {:8f}%".format(count, key, value*100), (x_coor,y_coor), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            print("{}. {}: {:8f}%".format(count, key, value*100))
            count += 1
            y_coor += 20
        cv2.imwrite("video_test/Super_Test_%d.jpg" % counter,img)
        cv2.imshow("test", img)
        counter += 1
        cv2.waitKey(1) 
    
    cv2.destroyAllWindows()