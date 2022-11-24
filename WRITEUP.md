[//]: # (Image References)

[image1]: ./Figure_2.png "EDA Figure"

### Project overview
Humans drive car mainly by eyes, the visual ability. Not only the object classification, but also the tracking of many objects. So the object detection, one of the AI technologies, is the most suitable technology for self driving car system.

The goals / steps of this project are the following:
* Load the Waymo Open Dataset
* Explore and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images by animaition

### Set up
Because I'm using the classroom workspace with the necessary libraries and data already available, thanks Udacity, there's no need to set up development environment. Just git clone my repository, then run it!

### Dataset
#### Dataset analysis

* The size of training set is ?
* The size of the validation set is ?
* The size of test set is ?
* The shape of an image is width 640px, height 640px, 3 color channels.
* The distribution of classes is: vehicle - 77.6%, pedestrian - 21.8%, cyclist - 0.6%

Here is an exploratory visualization of the data set, 10 images randomly. 
![alt text][image1]

### Training
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.002
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.004
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.008
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.004
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.011
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.008
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.206
 
INFO:tensorflow:Eval metrics at step 2500
I1124 07:02:31.414687 140146090903296 model_lib_v2.py:988] Eval metrics at step 2500
INFO:tensorflow:    + DetectionBoxes_Precision/mAP: 0.000549
I1124 07:02:31.422368 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Precision/mAP: 0.000549
INFO:tensorflow:    + DetectionBoxes_Precision/mAP@.50IOU: 0.002070
I1124 07:02:31.424026 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Precision/mAP@.50IOU: 0.002070
INFO:tensorflow:    + DetectionBoxes_Precision/mAP@.75IOU: 0.000114
I1124 07:02:31.425645 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Precision/mAP@.75IOU: 0.000114
INFO:tensorflow:    + DetectionBoxes_Precision/mAP (small): 0.000000
I1124 07:02:31.427284 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Precision/mAP (small): 0.000000
INFO:tensorflow:    + DetectionBoxes_Precision/mAP (medium): 0.003633
I1124 07:02:31.428808 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Precision/mAP (medium): 0.003633
INFO:tensorflow:    + DetectionBoxes_Precision/mAP (large): 0.007722
I1124 07:02:31.430592 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Precision/mAP (large): 0.007722
INFO:tensorflow:    + DetectionBoxes_Recall/AR@1: 0.000629
I1124 07:02:31.432336 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Recall/AR@1: 0.000629
INFO:tensorflow:    + DetectionBoxes_Recall/AR@10: 0.004492
I1124 07:02:31.434070 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Recall/AR@10: 0.004492
INFO:tensorflow:    + DetectionBoxes_Recall/AR@100: 0.011399
I1124 07:02:31.435876 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Recall/AR@100: 0.011399
INFO:tensorflow:    + DetectionBoxes_Recall/AR@100 (small): 0.000000
I1124 07:02:31.437248 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Recall/AR@100 (small): 0.000000
INFO:tensorflow:    + DetectionBoxes_Recall/AR@100 (medium): 0.008284
I1124 07:02:31.438935 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Recall/AR@100 (medium): 0.008284
INFO:tensorflow:    + DetectionBoxes_Recall/AR@100 (large): 0.206200
I1124 07:02:31.440628 140146090903296 model_lib_v2.py:991]  + DetectionBoxes_Recall/AR@100 (large): 0.206200
INFO:tensorflow:    + Loss/localization_loss: 0.844356
I1124 07:02:31.442041 140146090903296 model_lib_v2.py:991]  + Loss/localization_loss: 0.844356
INFO:tensorflow:    + Loss/classification_loss: 0.768587
I1124 07:02:31.443300 140146090903296 model_lib_v2.py:991]  + Loss/classification_loss: 0.768587
INFO:tensorflow:    + Loss/regularization_loss: 1.780340
I1124 07:02:31.444657 140146090903296 model_lib_v2.py:991]  + Loss/regularization_loss: 1.780340
INFO:tensorflow:    + Loss/total_loss: 3.393284
I1124 07:02:31.445983 140146090903296 model_lib_v2.py:991]  + Loss/total_loss: 3.393284

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
