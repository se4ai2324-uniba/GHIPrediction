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

# GHI PREDICTION
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

## Testing
The project has been tested with [pytest](https://docs.pytest.org/en/7.4.x/) and [great expectations](https://docs.greatexpectations.io/docs/). \
If you need to use these tools in our project you can type in your terminal:
```
pytest *path_of_the_module_containing_your_testing_functions*
 - or/and - 
python src/data/gx_test.py 
```
Quality of code has been assessed with [Pylint](https://pylint.readthedocs.io/en/stable/index.html) with an average score of **8.3**/10 on the non-autogenerated modules. \
You can check the code quality with the command:
```
pylint *path_of_module\folder_you_want_to_check* 
```

## APIs
The project incorporates also a module that implements a set of APIs. \
If you want to check them out you can run the [uvicorn](https://uvicorn.org) server just by running the python module _api.py_ with the command: 
```
python src/app/api.py 
```
The server will be accessible on your [https://127.0.0.1:8000](https://127.0.0.1:8000) \
You can also interact with the APIs through [Swagger](https://swagger.io) interface adding "/docs" to your localhost address [https://127.0.0.1:8000/docs](https://127.0.0.1:8000/docs). \
Alternatively you can explore the automatically-generated documentation via [redoc](https://github.com/redocly/redoc) adding "/redoc" instead [https://127.0.0.1:8000/redoc](https://127.0.0.1:8000/redoc). 

As for the fuction whithin the project, also the APIs have been tested with [pytest](https://docs.pytest.org/en/7.4.x/) and [Pylint](https://pylint.readthedocs.io/en/stable/index.html) (average score of 8.2/10).


## Orchestration
Our project includes a *dockerfile* and a *docker-compose.yaml*. \
Our initial step involved creating a straightforward Dockerfile, enabling the generation of an image within a Docker container. \
After this, we developed a Docker Compose file to serve as a services orchestrator, managing our current container and any future containers.

To create the orchestrator you can use the command: 
```
docker compose up
```

## GitHub Actions
Our project defines two different GitHub Actions, specifically:

-   **Pylint Action**: checks the non-autogenerated files for code correctness. It is triggered with every push, across all directiories.
-   **PreProcessing Action**: uses a [GitHub Secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) that contains the credentials for accessing the remote repository (in this case, Google Drive) through DVC.
This action replicates every step of our preprocessing pipeline, spanning from creating the dataset and applying preprocessing steps to spilitting it for the training phase. It can be triggered only manually.
-   **Tests Action**: uses a [GitHub Secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) that contains the credentials for accessing the remote repository (in this case, Google Drive) through DVC.
This action replicates every test of our pipeline. It can be triggered only manually.

## Code Carbon
We have integrated Code Carbon to monitor and assess the environmental impact of our model results, providing valuable insights into sustainability. You can access the detailed results in the associated [model card](https://github.com/se4ai2324-uniba/GHIPrediction/tree/main/models).

## Deployment & Monitoring
* **AWS deployment (nginx)** \
 Our app is up and running at [15.161.48.19](15.161.48.19). It has been deployed using [AWS](https://aws.amazon.com/). \
The deployment involves a Linux machine hosted on a European server with 2GB of RAM (extended to 4GB using local storage) and 28GB of storage. \
We utilize [nginx](https://www.nginx.com/) for serving the application.

* **Uptime** \
We ensure the continuous availability and performance monitoring of our deployed application through [Up time](https://betterstack.com/uptime).

* **Prometheus** \
[Prometheus](https://prometheus.io/) has been locally installed and run through the command
        ```
        prometheus --config.file=prometheus.yml
        ``` \
        This command starts the Prometheus server, collecting essential metrics needed for Grafana visualization.

* **Locust** \
To simulate web traffic and gather additional data for Grafana, we use [Locust](https://locust.io/)
Locust server is availabe at http://localhost:8089/ after the initialization through the command
        ```
        locust locustfile.py
        ``` 

* **Grafana** \
For comprehensive visualization of data generated by Locust and Prometheus, we use [Grafana](https://grafana.com/), which is locally installed. This allows us to customize and explore the metrics dashboards to gain insights into the performance of our application.

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
