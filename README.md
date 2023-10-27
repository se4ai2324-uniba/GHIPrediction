# GHI PREDICTION
---
language:
- en

tags:
- regression
- prediction
- machine_learning
- linear_regression
- xgbooster
- random_forest
- k_nearest_neighbors

datasets:
- national_solar_radiation_database

metrics:
- R2
- RMSE
---

## System Description:
The system will predict the Global Horizontal Irradiance (**GHI**) – *the amount of solar energy from the sun hitting a specific location*. \
It will do this by analyzing various physical data, including temperature, humidity, and Direct Normal Irradiance (**DNI**).
Information about our models can be found [here](https://github.com/se4ai2324-uniba/GHIPrediction/blob/main/models/README.md).

## Data card:
Information about our data can be found [here](https://github.com/se4ai2324-uniba/GHIPrediction/blob/main/data/README.md).


## Contributors:
- Francesco Didio [<f.didio2@studenti.uniba.it>];
- Giovanni Federico Poli [<g.poli4@studenti.uniba.it>]; 
- Donato Francioso [<d.francioso7@studenti.uniba.it>];

Belonging to the organization **se4ai2324-uniba**.


## How to
In order to use the system we suggest to:
1. Depending on your OS create a python environment with the command: 
    ```
    python3 -m venv name_of_your_env
    WINDOWS USERS:  call name_of_your_env/Scripts/activate
    MACOS USERS:    source name_of_your_env/bin/activate
    ``` 
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
3. Open the mlflow server:
    ```
    mlflow ui
    ```

4. Start the dvc pipeline: \
to let the system download the data files you have *to request the access to this* [*Google Drive repository*](https://drive.google.com/drive/folders/1zeHWwvDTYC7o_vcgWIwIpVO2VJdffhF4?usp=sharing)
    ```
    dvc pull
    dvc repro
    ```

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
