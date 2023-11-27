FROM python:3.11
RUN mkdir /ghi
COPY . /ghi

WORKDIR /ghi
RUN pip install -r requirements.txt
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt
# COPY . /fastAPIapp
# WORKDIR /fastAPIapp
EXPOSE 8000
WORKDIR /ghi/src/app
CMD ["python", "api.py"]
#launch docker on machine
#on terminal: docker build -t fasapiapp .
#on terminal: docker run -p 55000:55000 fastapiapp
