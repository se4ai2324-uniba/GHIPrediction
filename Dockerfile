FROM python:3.11
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /fastAPIapp
WORKDIR /fastAPIapp
EXPOSE 55000
CMD ["uvicorn", "app.api:app", "--host 0.0.0.0.", "--port 55000"]
#launch docker on machine
#on terminal: docker build -t fasapiapp .
#on terminal: docker run -p 55000:55000 fastapiapp
