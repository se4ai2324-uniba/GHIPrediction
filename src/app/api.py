"""module for APIs"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return{
        "message":"hi"
        }


