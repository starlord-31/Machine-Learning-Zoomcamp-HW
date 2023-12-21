![image](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/assets/144388508/958ec70e-ecce-4242-adf9-1c153b4d7c22)
# Predicting FIFA 24 Football Player Values

Dataset: https://www.kaggle.com/datasets/rehandl23/fifa-24-player-stats-dataset/

Problem Description: Predicting FIFA 24 Football Player Values

This project aims to develop a machine-learning model to predict the estimated value of FIFA football players. Using a dataset rich in player attributes, including demographics, physical traits, and performance metrics, the goal is to explore, clean, and preprocess the data. The focus is on experimenting with various machine learning models and selecting the most effective one for predicting player values. The end objective is to provide a useful tool for gamers, allowing them to estimate the in-game value of players based on their characteristics and skills.

## Running locally with gunicorn/waitress
1. Clone this repository on your computer.
3. Install dependencies from ```Pipfile``` by running command:
```Python
pipenv install
```
3. Activate virtual environment:
```Python
pipenv shell
```
4. Run service with gunicorn:
```Python
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```
Or with waitress:
```Python
waitress-serve --listen=0.0.0.0:9696 predict:app
```
5. Run [predict_test.py](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/blob/main/Capstone%201/predict_test.py) in a different terminal to see the predicted player value of a given player_attributes.

![image](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/assets/144388508/b381c598-8790-473c-8784-33f38bbd6686)

## Running locally with Docker
1. Build an image from a Dockerfile by the command:
```Python
docker build -t value_prediction .
```
2. Run service:
```Python
docker run --rm -it -p 9060:9060 -d  value_prediction
```
3. Run [predict_test.py](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/blob/main/Capstone%201/predict_test.py) in a different terminal to see the predicted player value of a given player_attributes.

## EBCLI to deploy service 
### Check if server works locally
1. First, awsebcli was installed using the following command:
```Python
pipenv install awsebcli --dev
```
2. The model was deployed in the cloud through **AWS Elastic Beanstalk**. For this, first, an application called ```player-value-prediction``` was created under the Docker platform, with the following command:
```Python
eb init -p "Docker running on 64bit Amazon Linux 2" player-value-prediction
```
3. It can now be tested locally executing:
```Python
eb local run --port 9696
```
4. Run [predict_test.py](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/blob/main/Capstone%201/predict_test.py) in a different terminal to see the predicted player value of a given player_attributes.

With the application address provided by AWS, another test script was created [cloud_test.py](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/blob/main/Capstone%201/cloud_test.py).

## Web service on AWS Elastic Beanstalk
### Test web service hosted on AWS Elastic Beanstalk
Running the [cloud_test.py](https://github.com/starlord-31/Machine-Learning-Zoomcamp-HW/blob/main/Capstone%201/cloud_test.py) script in a command window will return the prediction using the player-value-prediction-env environment and player-value-prediction application created in the AWS cloud.
