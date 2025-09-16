# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:45:46 2024

@author: COMP
"""

import math
dataset=[2,4,6,7,8.2]
sm=0
for i in range (len(dataset)):
    sm+=dataset[i]
    mean=sm/len(dataset)
deviation_sum=0
for i in range(len(dataset)):
    deviation_sum+=(dataset[i]-mean)**2
    psd=math.sqrt((deviation_sum)/len(dataset))
ssd=math.sqrt((deviation_sum)/len(dataset)-1)
print("Population standard deviation of the dataset is",psd)
print("sample standard deviation of the dataset is",ssd)