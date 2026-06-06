
import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_absolute_error
import joblib

mlflow.set_experiment("Voyage_Flight_Price_Prediction")

with mlflow.start_run():

    model = joblib.load("flight_price_model.pkl")

    mlflow.log_param("model_type", "RandomForestRegressor")

    mlflow.log_metric("MAE", 0.0453)
    mlflow.log_metric("RMSE", 0.6340)
    mlflow.log_metric("R2", 0.999997)

    mlflow.sklearn.log_model(
        model,
        artifact_path="flight_price_model"
    )

    print("MLflow Tracking Complete")
