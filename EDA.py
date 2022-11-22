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
import io

def display_images(batch, sub_ax):
    for data in batch:
        img = data['image'].numpy().astype("uint8")  
        sub_ax.imshow(img)
        for bb, cl in zip(data['groundtruth_boxes'].numpy(), data['groundtruth_classes'].numpy()):
            y1, x1, y2, x2 = bb
            rec = Rectangle((x1*img.shape[1], y1*img.shape[0]), (x2- x1)*img.shape[1], (y2-y1)*img.shape[0], 
                            facecolor='none', edgecolor=colormap[cl])
            sub_ax.add_patch(rec)
        sub_ax.axis('off')

dataset = get_dataset("/home/workspace/data/train/*.tfrecord")
colormap = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}
f, ax = plt.subplots(2, 5, figsize=(20, 10))
for i in range(10):
    x = i % 2
    y = i % 5
    batch = dataset.shuffle(1000, reshuffle_each_iteration=True).take(1)
    display_images(batch, ax[x, y])        
plt.tight_layout()
plt.show()
