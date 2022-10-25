# DL Optimization

## SGD with momentum

<img src="opt.assets/Screen Shot 2022-10-01 at 10.01.04 PM.png" alt="Screen Shot 2022-10-01 at 10.01.04 PM" style="zoom:50%;" /><img src="opt.assets/Screen Shot 2022-10-01 at 10.00.27 PM.png" alt="Screen Shot 2022-10-01 at 10.00.27 PM" style="zoom:50%;" />

原理：

<img src="opt.assets/Screen Shot 2022-10-01 at 9.54.58 PM.png" alt="Screen Shot 2022-10-01 at 9.54.58 PM" style="zoom:50%;" />



不足：

<img src="opt.assets/Screen Shot 2022-10-01 at 10.00.10 PM.png" alt="Screen Shot 2022-10-01 at 10.00.10 PM" style="zoom:50%;" />

## Nesterov Momentum

和Momentum的区别：where the gradient is evaluated

- Nesterov: gradient evaluated **after current velocity** is applied

- can interpret Nesterov as attempting to **add a correction factor** to the standard momentum method：

  <img src="opt.assets/Screen Shot 2022-10-01 at 9.57.49 PM.png" alt="Screen Shot 2022-10-01 at 9.57.49 PM" style="zoom:50%;" />

  <img src="opt.assets/Screen Shot 2022-10-01 at 10.01.59 PM.png" alt="Screen Shot 2022-10-01 at 10.01.59 PM" style="zoom:50%;" />

  

## Adagrad, Adadelta, RMS Prop

### Adagrad

scale by intersely proportional to accumulated square of sum of partial derivative 

results in **greater progress in gentler change of directions**

优点：

good for sparse data

more robust than SGD

缺点：

accumulated squared gradients gets infinitely small

### **Adadelta** 

restricted window of accumulate sum to fixed-size

### **RMSProp** 

change accumulated sum to exponentially weighted moving average

gradient surface is not flat: gradients usually starts out large and flattens later -- allow lr to adapt to changing local topology 

- 容易实现，易用
- 实际应用中常用

## Adam

Adam: RMSProp + momentum 的变种之一

区别：

- momentum项: 直接使用1st-order rescaled gradient(exp. weighted moving average)去估计gradient，然后加到previous momentum(原来的v）上
- bias correction for the both 1st-order momentum + 2nd-order momentum (RMSProp没有)

**go-tos for empirical use: 实际应用中常用**

### AdamW: 

Adam w/ weight decay 

*weight decay和L2 regularization对于sgd来说是**相同**的，但对于更复杂的优化算法不同。*

## 调优

[10 Hyperparameters to keep an eye on for your LSTM model — and other tips - Medium](https://medium.com/geekculture/10-hyperparameters-to-keep-an-eye-on-for-your-lstm-model-and-other-tips-f0ff5b63fcd4) 

 [GA（遗传算法）优化LSTM神经网络-CSDN博客](https://blog.csdn.net/Vertira/article/details/122403571) 