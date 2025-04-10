from mlflow.tracking import MlflowClient
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000/")

client = MlflowClient()
# experiment = client.get_experiment_by_name("ML-Model-1") # your experiment name
experiment = client.get_experiment_by_name("ML-Model-1")
print("Experiment ID:", experiment.experiment_id)

runs = client.search_runs(experiment_ids=[experiment.experiment_id])
for run in runs:
    print("Run ID:", run.info.run_id)