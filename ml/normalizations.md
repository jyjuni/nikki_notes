## Batch Normalization, in general

 [A Gentle Introduction to Batch Normalization for Deep Neural Networks](https://machinelearningmastery.com/batch-normalization-for-training-of-deep-neural-networks/)  [Batch Normalization: Accelerating Deep Network Training b y Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf) 

internal covariate shift（内部协变量偏移）

probelm: 

- model is updated layer-by-layer backward from the output to the input using an estimate of error *under the assumption that the other layers do not change. In practice, we update all of the layers simultaneously.*

- **internal covariate shift:** for deep networks, change in the distribution of inputs to layers deep in the network
- cause learning to **forever chase a moving target**

### Batch Normalization

#### solution

- standardizes the inputs to a layer for each mini-batch
  - means that assumptions the subsequent layer makes about the **spread and distribution of inputs during the weight update will not change**, at least not dramatically

- **stabilizing** the learning process: smooths and simlifies optimization function
- dramatically reducing the **number of training epochs** required to train deep networks
- **regularizing** effect: reducing generalization error like activation regularization

#### learnable param $\gamma$, $\beta$

> Note that simply normalizing each input of a layer may change what the layer can represent. For instance, normalizing the inputs of a sigmoid would constrain them to the linear regime of the nonlinearity.

- make sure that the transformation inserted in the network **can represent the identity transform** （需要的时候可以保持原分布不变换）

$$
y^{(k)} = \gamma ^ {(k)} \hat x ^{(k)} + \beta ^ {(k)}
$$

- $\gamma$, $\beta$ are learned along with the original model parameters, and restore the representation power of the network.

### Batch Renormalization

 [1702.03275.pdf](https://arxiv.org/pdf/1702.03275.pdf) 

问题：如果训练的batch size太小或没有代表性，训练和预测数据的差异会影响模型效果。

解决方法：BN +  *per-dimension correction*



### 位置

activation前

#### activation后

## BN vs LN

### Batch Normalization

batch-wise per feature, across samples

<img src="normalizations.assets/batch-normalization-example.png" alt="Batch Normalization Example" style="zoom:50%;" />

- 对于小batch size无效

- 训练和预测阶段步骤不同

  - 训练：维护mean和variance的moving average [Moving average in Batch Normalization](https://jiafulow.github.io/blog/2021/01/29/moving-average-in-batch-normalization/) 
    $$
    \mu = \alpha \mu^{(k)} + (1-\alpha)\mu \\
    \sigma = \alpha \sigma^{(k)} + (1-\alpha)\sigma
    $$
  
  - 预测：使用runing mean & variance的无偏期望值<img src="normalizations.assets/Screen Shot 2022-10-04 at 11.38.39 PM.png" alt="Screen Shot 2022-10-04 at 11.38.39 PM" style="zoom: 33%;" />
  
  > 需要用moving average的原因：
  >
  > 在训练中会穿插验证（使用验证集数据进行预测），这时全部batch的训练还没有结束，因此可以使用runing mean & variance进行预测。
  >
  > > Using moving averages instead, we can track the accuracy of a model as it trains.

### Layer Normalization

layer-wise per sample, across features

<img src="normalizations.assets/layer-normalization.png" alt="Layer Normalization" style="zoom:50%;" />

- 训练与预测阶段相同