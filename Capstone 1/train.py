#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm


# Loading the dataset

df = pd.read_csv('/mnt/e/Downloads/ML_Zoomcamp/Capstone_1/cleaned.csv', encoding='latin-1')

# Setting up the validation framework

from sklearn.model_selection import train_test_split
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

len(df_train), len(df_val), len(df_test)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.value_logs.values
y_val = df_val.value_logs.values
y_test = df_test.value_logs.values
y_full_train = df_full_train.value_logs.values

del df_train['value']
del df_val['value']
del df_test['value']
del df_full_train['value']

del df_train['value_logs']
del df_val['value_logs']
del df_test['value_logs']
del df_full_train['value_logs']


# Scaling the data

from sklearn.preprocessing import MinMaxScaler

X_train = df_train.values
X_val = df_val.values
X_test = df_test.values
X_full_train = df_full_train.values

# Initialize a scaler
scaler = MinMaxScaler()

# Fit the scaler to the training features and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform the validation and test features using the same scaler
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

X_full_train_scaled = scaler.fit_transform(X_full_train)


# Model building

from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV

params = {'colsample_bytree': [0.4], 'gamma': [0.1], 'learning_rate': [0.05], 'max_depth': [6], 'min_child_weight': [7], 'n_estimators': [210]}

# Initialize an XGBoost Regressor
xgb = XGBRegressor(random_state=42)

# Initialize the Grid Search CV
grid_search = GridSearchCV(estimator=xgb, param_grid=params, cv=3, n_jobs=-1, verbose=2)

# Fit the Grid Search to the data
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters
best_params = grid_search.best_params_


from sklearn.metrics import mean_squared_error

# Training the model
# Train a new XGBoost with the best parameters
best_xgb = XGBRegressor(**best_params, random_state=42)
best_xgb.fit(X_train_scaled, y_train)

# Predictions on the validation set
# Make predictions on the scaled validation set
y_val_pred = best_xgb.predict(X_val_scaled)

# Undo the log transformation on the predictions
y_val_pred_exp = np.expm1(y_val_pred)

# Undo the log transformation on the actual target values
y_val_exp = np.expm1(y_val)

# Calculate the RMSE of the predictions
rmse_val = np.sqrt(mean_squared_error(y_val_exp, y_val_pred_exp))

# Print the RMSE
print(f'Validation RMSE: {rmse_val}')


# Predictions on the test set
best_xgb.fit(X_full_train_scaled, y_full_train)
y_test_pred = best_xgb.predict(X_test_scaled)

# Undo the log transformation on the predictions
y_test_pred_exp = np.expm1(y_test_pred)

# Undo the log transformation on the actual target values
y_test_exp = np.expm1(y_test)

# Calculate the RMSE of the predictions
rmse_test = np.sqrt(mean_squared_error(y_test_exp, y_test_pred_exp))

# Print the RMSE
print(f'Test RMSE: {rmse_test}')


# Save the model
import pickle

filename = 'finalized_model.bin'
pickle.dump(best_xgb, open(filename, 'wb'))