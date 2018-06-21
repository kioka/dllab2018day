
# coding: utf-8

# In[2]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


# In[3]:


import chainer
import chainer.links as L
import chainer.functions as F


# In[6]:


import numpy as np
import os
import cv2

def getDataSet():
    
    # dataset
    train_imgs = []
    train_labels = []
    
    # ファイルリスト取得
    f = open('train_labels.txt')
    imgList = f.readline()
    
    for img in imgList:
        items = img.split(" ") 
        
        # 画像データの読み込
        imgSrc = cv2.imread("../sample/train_labels.txt" + items[0], 0)
        train_imgs.append(imgSrc)
        
        # クラスの読み込み
        train_labels.append(items[1])
    
    return train_imgs,train_labels

# データ・セットの読み込み
train_imgs, train_imgs = getDataSet()
train_imgs = np.array(train_imgs).astype(np.float32)
train_imgs = np.array(train_imgs).astype(np.int32)

