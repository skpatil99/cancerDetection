import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import cv2
import sys
import os
import numpy as np
from random import shuffle
from tqdm import tqdm
from tflearn.helpers.evaluator import Evaluator
import tensorflow as tf

def CNN(path):
    LR = 0.9e-3
    IMG_SIZE=150
    img_tensor=[]

    tf.reset_default_graph()
    convnet = input_data(shape =[None, IMG_SIZE, IMG_SIZE, 3], name ='input')

    convnet = conv_2d(convnet, 32, 3, activation ='relu') #32 neurons create IMG_SIZE*IMG_SIZE*32
    convnet = max_pool_2d(convnet, 3) #stride of size 3

    convnet = conv_2d(convnet, 64, 3, activation ='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 128, 3, activation ='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 256, 3, activation ='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 128, 3, activation ='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation ='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 32, 3, activation ='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = fully_connected(convnet, 200, activation ='relu')
    convnet = dropout(convnet, 0.9)

    convnet = fully_connected(convnet,2, activation ='softmax')
    convnet = regression(convnet, optimizer ='adam', learning_rate = LR,
          loss ='categorical_crossentropy', name ='targets')

    model = tflearn.DNN(convnet,tensorboard_verbose=3)
    model.load('/home/sanket/Desktop/WebApp/Detection/Leukemia/my_model.tflearn')

    img = cv2.imread('/home/sanket/Desktop/WebApp/Detection/media/'+str(path))
    img = cv2.resize(img, (150, 150))
    img_tensor.append(np.array(img))

    result=model.predict(img_tensor)
    ind=np.argmax(result)
    if ind==1:
    	return "Cancerous"
    else:
    	return "Non-Cancerous"
