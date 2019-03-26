'''
Step 1: Loads data set from our csv file into a pandas df
Step 2: Partitions into training and test sets
Step 3: "Trains" KNN, and then predicts for test.
Step 4: Important metrics gathered on KNN classifier (accuracy for now. Will want precision, recall, and probably others)
'''

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### Step 1: Loads data set from our csv file into a pandas df
pwd = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(pwd, "../data/labled_dataset.csv")
data = pd.read_csv(data_path)

### Step 2: Partitions into training and test sets


### Step 3: "Trains" KNN, and then predicts for test.


### Step 4: Important metrics gathered on KNN classifier
