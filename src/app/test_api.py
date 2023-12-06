"""module for AIPs tesing"""
from http import HTTPStatus
import warnings
import pytest
from api import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_root():
    """tests the base root"""
    response= client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json()=={"name":"GHI-Prediction",
        "message":"Welcome to GHI-Prediction Project",
        "github":"https://github.com/se4ai2324-uniba/GHIPrediction",
        "contributors":["Francesco Didio","Giovanni Federico Poli","Donato Francioso"]}


def test_best_results():
    """tests best results API"""
    response= client.get("/best_model/")
    assert response.status_code == HTTPStatus.OK

    #check if name and params are respectively str and dict
    assert isinstance(response.json()["name"], str)
    assert isinstance(response.json()["params"], dict)

    assert response.json()["name"] == "XgBooster"

    #check if R2 and RMSE are valid values
    assert isinstance(float(response.json()["r2"]), float)
    assert isinstance(float(response.json()["rmse"]), float)


def test_model_list():
    """tests the models list API"""
    response= client.get("/models/")
    assert response.status_code == HTTPStatus.OK

    # Check if the response contains the expected items
    assert "description" in response.json()
    assert "lista" in response.json()

    # Check the data types of the response values
    assert isinstance(response.json()["description"], str)
    assert isinstance(response.json()["lista"], list)

    assert response.json()["description"] == "I modelli usati sono: "

    # check specific model names
    expected_models = ["Linear Regression", "Random Forest Regressor",
    "XGBooster", "K-Neighboor Regressor"]
    assert response.json()["lista"] == expected_models


#to do -> check if it goes always in exception
# @pytest.mark.parametrize("model_name",["KNR","XGB","RF","LR"])
# def test_model_results(model_name):
#     """tests the model's results API"""
#     try:
#         response= client.get(f"/model/{model_name}/params")
#         assert response.status_code == HTTPStatus.OK
#         assert "params" in response.json()
#         assert isinstance(response.json()["params"], dict)
#     except ValueError as e:
#         print(f"error: {e}")


def test_predict_ghi():
    """tests the prediction API"""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        payload = {"temperature": 25.0, "dni": 500, "humidity": 50}
        response = client.post("/prediction", json=payload)
        assert response.status_code == HTTPStatus.OK

        # Check if the response contains the expected key

        assert "predicted_GHI" in response.json()

        # Check the data type of the predicted_GHI value
        assert isinstance(response.json()["predicted_GHI"], float)
