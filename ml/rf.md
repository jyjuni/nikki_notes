# Random Forest

## Concepts



## Packages

scikit-learn:

`sklearn.ensemble.RandomForestClassifier`

- no support for categorical features, need one-hot encoding
- cannot specify metrics

[template using sklearn](../fraud_prediction/fraud_rf.ipynb)

h2o:

`h2o.estimators.random_forest`

- support categorical features
  - convert column type to `.asfactor()`
- specify metrics
  - `stopping_metric='auc'`
- partial plots
  - `model.partial_plot()`
  - use?

[example using h2o](https://github.com/JifuZhao/DS-Take-Home/blob/master/04.%20Identifying%20Fraudulent%20Activities.ipynb)



