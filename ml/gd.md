# 梯度下降 Gradient Descent

## 梯度消失与爆炸问题
### 梯度消失

$|gradient| \rightarrow 0$
- RNN, $|single\ gradient| < 1$
- sigmoid

### 梯度爆炸
$|gradient| \rightarrow \infin$
- RNN, $|single\ gradient| > 1$

## 激活函数
> "I think we are in a stage of alchemy and we haven't invented chemistry yet."

### Sigmoid
> 梯度消失问题

### Relu
> 为什么relu不会有梯度消失？
Expectation: 一半的时间梯度不会为0

### LeakyRelu
改善了Relu，负的部分也不为0。
表现大体和Relu相同

----
*可能因为上述原因，在很多超大的神经网络中，存在很多“dead neurons”（权值一直为0）。但因为神经元数巨大，所以不造成影响。*


