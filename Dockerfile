FROM python:3.11
RUN mkdir /ghi
COPY . /ghi

WORKDIR /ghi
RUN pip install -r requirements_docker.txt

EXPOSE 8000
WORKDIR /ghi/
CMD python src/app/api.py

