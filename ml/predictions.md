# 预测

## Class Imbalance

### 1.重采样

[API](https://imbalanced-learn.org/stable/over_sampling.html)

#### Random Oversampling

#### SMOTE

- 

#### SMOTE-NS

- 可处理categorical features

#### Comparison

> While the [`RandomOverSampler`](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html#imblearn.over_sampling.RandomOverSampler) is over-sampling by duplicating some of the original samples of the minority class, [`SMOTE`](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE) and [`ADASYN`](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.ADASYN.html#imblearn.over_sampling.ADASYN) generate new samples in by interpolation. However, the samples used to interpolate/generate new synthetic samples differ. In fact, [`ADASYN`](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.ADASYN.html#imblearn.over_sampling.ADASYN) focuses on generating samples next to the original samples which are wrongly classified using a k-Nearest Neighbors classifier while the basic implementation of [`SMOTE`](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE) will not make any distinction between easy and hard samples to be classified using the nearest neighbors rule. Therefore, the decision function found during training will be different among the algorithms.

### 2.Class Weight

****