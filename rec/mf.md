# Matrix Factorization

 [Recommendation Systems Colab - Colaboratory](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/recommendation-systems/recommendation-systems.ipynb?utm_source=ss-recommendation-systems&utm_campaign=colab-external&utm_medium=referral&utm_content=recommendation-systems&authuser=1#scrollTo=Jz5bqVbFo4uJ) 

### Regularization

#### parameter regularization

common l2 regularization term on the embedding matrices

#### global regularization

pushes the prediction of any pair towards zero, called  *gravity*.

## Similarity Measure

[lab example](https://colab.research.google.com/drive/1o03RO6m1zawdUvfIDKd7iAtva-3dt4iQ?authuser=1#scrollTo=SOxdxqpKo4uB)

recommendations with dot-product and cosine are different:

- dot-product

  -  tends to recommend popular movies:

    because in matrix factorization models, the norm of the embedding is often correlated with popularity (popular movies have a larger norm), which makes it more likely to recommend more popular items.

