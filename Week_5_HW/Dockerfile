FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["predict_Q6.py", "Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

EXPOSE 9695

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9695", "predict_Q6:app"]