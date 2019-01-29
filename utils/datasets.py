from scipy.io import loadmat
import pandas as pd
import numpy as np
from random import shuffle
import os
import cv2


def get_labels(dataset_name):
    if dataset_name == 'fer2013':
        return {0:'angry',1:'disgust',2:'fear',3:'happy',
                4:'sad',5:'surprise',6:'neutral'}
    else:
        raise Exception('Invalid dataset name')

