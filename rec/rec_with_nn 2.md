# 推荐系统网络

## Softmax Model





### Two-tower network

also learn a network for item



## Negative Sampling

[Negative Sampling - Google Developers](https://developers.google.com/machine-learning/recommendation/dnn/training#negative-sampling)

**<u>problem:</u>**

- use all items
  - computationally too expensive

- sample positive items only
  - folding

**solution:** use negative sampling



### Folding

### Sampling Strategy

- sample uniformly
- give higher weights on **hard negatives**
  - higher probability to items j with higher score $\psi(x) \cdot V(j)$
  - intuitively, theses examples contribute the most to the gradient



### Matrix Factorization vs. DNN (softmax)

<img src="rec_with_nn.assets/Screen Shot 2022-09-09 at 3.05.17 PM.png" alt="Screen Shot 2022-09-09 at 3.05.17 PM" style="zoom:50%;" />

in summary:

- MF: 
  - better for large corpora
  - easier to scale, cheaper
  - less prone to folding

- DNN：

  - capture personalized preference better

  - harder to train, expensive

  - preferable for **scoring**:

    - because DNN models can use more features to better capture relevance.
    - usually acceptable for DNN model to fold: because you usually cares about ranking a pre-filtered set of candidates assumed to be relevant

    