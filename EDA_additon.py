from utils import get_dataset
import glob
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from PIL import Image
import numpy as np
import tensorflow as tf
from waymo_open_dataset import dataset_pb2 as open_dataset

dataset = get_dataset("/home/workspace/data/train/*.tfrecord")
cls_num = {1: 0, 2: 0, 4: 0}
for data in dataset.take(1000):
    for cl in data['groundtruth_classes'].numpy():
        cls_num[cl] += 1
        
print(cls_num)
    