import time
from locust import HttpUser, task, between

class TestUser(HttpUser):

    wait_time = between(1, 5)

    @task
    def get_best_model(self):
        self.client.get('/best_model', name = 'Get_Model')

    @task
    def get_info(self):
        self.client.get('', name = 'Get_info')

    @task 
    def get_prediction(self):
        self.client.post("/prediction", json={"temperature":0,"dni":0,"humidity":0}, name = 'Get_Prediction')