FROM python:3.11
RUN mkdir /ghi
COPY . /ghi

WORKDIR /ghi
RUN pip install -r requirements_docker.txt

RUN dvc remote modify myremote --local gdrive_service_account_json_file_path ghi-prediction-6869d952fb04.json

RUN dvc pull || true

RUN dvc repro

EXPOSE 8000
WORKDIR /ghi/
CMD python src/app/api.py