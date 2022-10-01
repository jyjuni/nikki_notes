# Object Recognition

 [Convolutional Neural Networks - Object Detection | Coursera](https://www.coursera.org/learn/convolutional-neural-networks/home/week/3) 

## Context

[Sapir–Whorf hypothesis](https://en.wikipedia.org/wiki/Linguistic_relativity)

- people's perceptions are relative to their spoken language

### R-CNN

two stage pipeline: first classify where the interesting image regions are, then do a classification of each region

### Fast R-CNN and Faster R-CNN

allow do both stage jointly, first propose candidate window, then classify them, so train this end-to-end s.t. gradients can be propagated back through all. if you learn to propose windows, if would then be useful for classification. 

#### Fast R-CNN

subsample the windows

Conv feature map: spatiallly, **"where"** the windows are 

ROI feature vector: encoded content, **"what"**  to propagate through

**softmax:** score - should you continue processing it

**regressor:** what is this, why is that out there 

#### Faster R-CNN

output a score(trainable) for every single window, pick top 300

**region proposal network**: 

propose region-cropping which is differentiable

**RoI Pooling:** max-pooling, combining where+what -  reszing the feature vector so that each vector is of same size, to feed into classification network



## Detection, Segmentation

### detection

bounding box

### segmentation

#### semantic segmentation

object categories: bird vs sky

#### instance segmentation

per instance



### Fully Convolutional Networks

raw image(pixels) as input, output image encoding what all the categories are

everything is a convolution

no resizing

if you keep doing convolution you will get another image out



### U-Net

**idea:** tradeoff between

- do want to integrate some global information (down-sampling)
  - if you never resize, hard to get long-range (cross-pixels) connections eg: pixel of a bed

- also want to include enough information and details

**encoder**: downsample

more and more global information

**decoder**: upsample

increase resolution

**skip connections**: avoid bottleneck, propagate to same-resolution layers

## Residual Network

before ResNet: up to 20 layers

after: thousands of layers possible

<img src="object_recogniton.assets/Screen Shot 2022-08-21 at 4.02.46 PM.png" alt="Screen Shot 2022-08-21 at 4.02.46 PM" style="zoom:50%;" />

**intuition**: 56-layer network should perform (in training error) at least  as good as 20-layer, because the rest 36 layers could learn to do nothing.

<img src="object_recogniton.assets/Screen Shot 2022-08-21 at 4.04.48 PM.png" alt="Screen Shot 2022-08-21 at 4.04.48 PM" style="zoom:50%;" />

**idea**: make it easy to learn to do nothing 

- forward: F(·) can learn to output 0, many ways to do that. but without residual F(x) has only one way to propagate identity(hard to learn that as example above)

- backwards: gradients split at plus gate, so even F(x) mess up with the gradient (eg: vanishes), x is still able to propagate the gradient back

**note:** can only do resnet if input and output dimensions of residual block are same-size

### Reversible Residual Network

computational trick to save memory(trade time for space)



# Deeplearning.ai

## localization vs detection

### Classification with Localization

single-instance

### detection

multi-instance

## Classification with Localization

image -> ConvNet -> vector feature(n classes) -> softmax(n classes)

<img src="object_recogniton.assets/Screen Shot 2022-08-24 at 3.06.44 PM.png" alt="Screen Shot 2022-08-24 at 3.06.44 PM" style="zoom:50%;" />

## Sliding windows detection algorithm



### Convolutional Implementation



## YOLO algorithm

> "YOLO may not be the best detector, but it is the most colorful one."

<img src="object_recogniton.assets/Screen Shot 2022-08-24 at 4.04.03 PM.png" alt="Screen Shot 2022-08-24 at 4.04.03 PM" style="zoom:50%;" />

### single-shot vs two-shot:

**end-to-end**/single-shot detector: both detection and classification

looking for specific bounding boxes

vs two-shot/two-stage: first draw bounding box, then classify it



**yolo's contribution**: 

all focus on speed 

single-shot detector

- like object localization task (vs sliding window):
  - output bounding boxes of any aspect ratio
  - output more precise coordinates that aren't just dictated by the stripe size of the sliding window classifier

- **convolutional implementation:** choose the conv layers and the max pool layers so that this eventually maps to a 3 by 3 by 8 output volume.
  - can extract information $p_c$, bounding box coordinates $b_x, b_y, b_h, b_w$ and class labels $c_1,c_2,c_3$ from each $\mathbf y$

**problems**

multiple object assigned to one grid cell? 

- use finer grid to reduce chance

one instance across grid

- assign object to grid cell by its midpoint

- can go across grid(bw, bh > 1)

  <img src="object_recogniton.assets/Screen Shot 2022-08-24 at 4.06.37 PM.png" alt="Screen Shot 2022-08-24 at 4.06.37 PM" style="zoom:30%;" />

### IoU (Intersection over Union)

<img src="object_recogniton.assets/Screen Shot 2022-08-24 at 4.24.48 PM.png" alt="Screen Shot 2022-08-24 at 4.24.48 PM" style="zoom:50%;" />

### Non-max Suppresion

make sure each object is detected only once

<img src="object_recogniton.assets/Screen Shot 2022-08-24 at 4.32.43 PM.png" alt="Screen Shot 2022-08-24 at 4.32.43 PM" style="zoom:50%;" />

**problem:** calculate probability for each class i:  $p_{i} = p_c \cdot c_i$

 [Weekly Assignment - Car detection with YOLO](https://www.coursera.org/learn/convolutional-neural-networks/programming/3VCFG/car-detection-with-yolo/lab?path=%2Fnotebooks%2FW3A1%2FAutonomous_driving_application_Car_detection.ipynb#) 

### Anchor boxes

detect overlapping objects

<img src="object_recogniton.assets/Screen Shot 2022-08-24 at 4.40.30 PM.png" alt="Screen Shot 2022-08-24 at 4.40.30 PM" style="zoom:50%;" />

problem:

- three objects but two anchor boxes
- two object with exactly same-shape anchor box
  - later YOLO version: k-means to find similar-shape objects

more for specification

*in practice, this does not happens often in 19 by 19 grid cell*

### Incremental Improvements

v1-v3 introduced by [Joseph Redman](), later Alex and Glenn

#### **yolo v1**

original resolution

limitation: 

"all things equall": struggle with small objects, especially further from frames

cap for number of classes: cannot have more than 10 objects in a row



#### **yolo v2 (yolo-9000)**

 *"faster, better, stronger"*

better

BN layer

higher resolution classifier -> 448

anchor box

dimension clutters using k-means

fine-grained features

Darknet-19

(all FC layer removed -- faster)

**hierachical classification** -- stronger

#### yolo v3

darknet-53 as feature extractor 

residual connections [Alphago paper graph]()

implemented in other framework(keras); connect to pytorch by Glenn Jocher for particle research

#### yolo v4

data augmentation and preprocessing

also in other framework; 

#### yolo v5

(no paper, just a github repo)

fully implemented on pytorch by Glenn Jocher

getting to production quickly: ease-of-use, exportabiity, memory requirements, speed, mAP, market size



*non-sequential, a community that all forks make contribution to it*



## Region Proposals

tries to pick just a few regions that makes sense to run your continent crossfire.

segmentation algorithm: find ~2000 blobs of potention interests

**R-CNN:**

Propose regions. classify proposed regions **one at a time**. output label + bounding box

**Fast R-CNN:**

Propose regions. use **convolution implementation** of sliding windows to classify all the proposed regions.

(roughly similar to convolution implementation)

**Faster R-CNN:**

starting point: clustering step in Fast R-CNN to propose the regions are relatively slow

use **convolutional network** to propose regions.

*Faster R-CNN usually still quite slower than YOLO*

> Andrew's notes on region proposal:
>
> I think that region proposal is an interesting idea by that not having two steps-- first propose region and then classify it--being able to do everything all at the same time, similar to the YOLO or the You Only Look Once algorithm that seems to me like a more promising direction for the long term. 



 [Different YOLO versions under 10 mins - YouTube](https://www.youtube.com/watch?v=KWK4e7QNW-4) 