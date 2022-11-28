[//]: # (Image References)

[image1]: ./Figure_2.png "EDA Figure"
[image2]: ./Iter1_loss.png "Iteration 1 Loss Graph"
[image3]: ./Iter2_loss.png "Iteration 2 Loss Graph"
[image4]: ./Iter3_loss.png "Iteration 3 Loss Graph"
[image5]: ./Iter5_loss.png "Iteration 5 Loss Graph"
[image6]: ./Iter5_testpic1.png "Iteration 5 Inference video shotcut"
[image7]: ./aug1.png "augmentation 1"
[image8]: ./aug2.png "augmentation 2"

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

* The shape of an image is width 640px, height 640px, 3 color channels.
* The distribution of classes is: vehicle - 77.6%, pedestrian - 21.8%, cyclist - 0.6%

Here is an exploratory visualization of the data set, 10 images randomly. 
![alt text][image1]

### Training
#### Reference experiment
#### Iteration 1: 
Based on Project Instructions, I trained the first model by default pipeline.config. But as shown in the figure, the loss curve is not ideal and fluctuates up and down. The mAP is close to zero. Observing the generated animation, the vehicle cannot be recognized in the backlit scene, and the night scene has misrecognition problem.
![alt text][image2]
 
 * Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.001
 * Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.002
 * Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 * Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 * Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.004
 * Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.008
 * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.001
 * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.004
 * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.011
 * Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 * Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.008
 * Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.206
 
#### Improve on the reference
#### Iteration 2: 
I heard that increasing the batch_size can solve the training up and down oscillations, and it is easy to converge, so I increased the batchsize to 4 in this iteration. The loss curve is stable and convergent (see the bottom curve), and the mAP is slightly increased. The daytime scene recognition rate is very good (vehicles that are only partially displayed are not recognized). Two vehicles are identified in a backlit scene. The night scene is still not recognized at all, but the misrecognition problem of iteration 1 is gone.
![alt text][image3]

  * Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.031
  * Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.072
  * Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.026
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.010
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.128
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.134
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.009
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.039
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.071
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.036
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.214
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.262
 
 #### Iteration 3: 
The batchsize is changed to 8, the loss curve is further reduced (see the bottom curve), and the mAP is also increased. The daytime scene recognition rate is perfect, and vehicles that are only partially displayed are also recognized. Backlit scenes are also perfect. The scene recognition effect at night is also very good (the oncoming car is not good at a distance, but it can be recognized after approaching). The training time is long, 4 minutes per 100epoch.
![alt text][image4]
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.092
  * Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.174
  * Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.088
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.032
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.355
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.384
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.021
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.096
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.145
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.085
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.468
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.489

 #### Iteration 4: 
The batchsize was changed to 4, and the following augmentation options were added. But I found the loss curve did not converge, so I interrupted the training.
```
  data_augmentation_options {
    random_rgb_to_gray {
    probability: 0.2
    }
  }
  data_augmentation_options {
    random_adjust_brightness {
    max_delta: 0.5
    }
  }
```
 ![alt text][image7] ![alt text][image8]

 #### Iteration 5:
 The batchsize is changed to 8, plus the same augmentation options for iteration 4. The loss curve is a little oscillating, and the mAP is not as good as iteration 3. However, the night scene recognition effect is particularly good. the problem of not recognizing the oncoming car at a distance in iteration 3(without augmentation) has been perfectly solved (as shown in the screenshot).
 ![alt text][image5]
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.089
  * Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.169
  * Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.082
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.030
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.324
  * Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.394
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.020
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.094
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.140
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.082
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.437
  * Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.443
 ![alt text][image6]
