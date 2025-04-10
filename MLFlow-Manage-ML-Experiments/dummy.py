from mlflow.tracking import MlflowClient

client = MlflowClient()
version_info = client.get_model_version("LogisticRegression_MLFlow_Staging", "2")
print("Source URI:", version_info.source)