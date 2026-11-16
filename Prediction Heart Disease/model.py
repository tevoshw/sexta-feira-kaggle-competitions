import joblib
import xgboost, lightgbm, catboost


model =  joblib.load('Prediction Heart Disease/prediction_heart_disease.joblib')['LGBM_Default']

print(model)