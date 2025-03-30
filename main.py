from tensorflow import keras
import random
import os
import cv2 as cv

husky_train=os.listdir('data/train/husky')
wolf_train=os.listdir('data/train/wolf')

print(random.sample(husky_train,4))