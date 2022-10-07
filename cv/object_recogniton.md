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



