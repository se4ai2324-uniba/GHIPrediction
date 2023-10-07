# GHI PREDICTION

## Project Title: 
GHI-Prediction

## Model Description:
The system will predict the Global Horizontal Irradiance (**GHI**) – *the amount of solar energy from the sun hitting a specific location*. \
It will do this by analyzing various physical data, including temperature, humidity, and Direct Normal Irradiance (**DNI**).

## Contributors:
- Francesco Didio [<f.didio2@studenti.uniba.it>];
- Giovanni Federico Poli [<g.poli4@studenti.uniba.it>]; 
- Donato Francioso [<d.francioso7@studenti.uniba.it>];

Belonging to the organization **se4ai2324-uniba**.

## Intended Use:
The prediction is essential for optimizing solar energy systems, helping them operate more efficiently. \
The devices used for collecting data can be quite costly, making it beneficial to predict this information in advance. This study aims to develop a method for forecasting the Global Horizontal Irradiance (GHI), the main value in photovoltaic installations, using physical data like temperature, relative humidity, and direct normal irradiance (DNI). By obtaining this data in advance through physical instruments, we can potentially reduce measurement expenses.

## Model Type & Framework:
The System uses **Scikit-learn** framework for preprocessing the data and for importing the models that are:
- XGbooster 
- Linear Regression 
- Random Forest Regressor 
- KNeighbors Regressor.

## Evaluation Metrics:
The System will be evaluated with **R2** and **RMSE** metrics.
- R2 assesses how well the model explains variance in the data;
- RMSE measures the average size of prediction errors.

These metrics are often used together to evaluate the overall performance of regression models, with R2 indicating goodness of fit and RMSE indicating the accuracy of predictions.

## Hyperparameters:
Hyperparameters tuning allows to tweak the model performance for optimal results. \
In order to find the best hyperparameters it has been used the `GridSearchCV` that exhausts all the possibile combination between them, splitting the dataset in 10 folds.
- XGBooster: `learning_rate: 0.1`, `max_depth: 5`, `n_estimators: 100`;
- KNeighbors Regressor: `n_neighbors: 9`, `metric: euclidean`;
- Random Forest: `max_depth: 6`, `n_estimators: 140`; 

## Performance:
......

