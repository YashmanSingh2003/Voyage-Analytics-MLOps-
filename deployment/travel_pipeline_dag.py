
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def load_data():
    print("Loading travel data")

def train_model():
    print("Training flight price model")

def evaluate_model():
    print("Evaluating model")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1)
}

dag = DAG(
    dag_id="travel_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

load_task = PythonOperator(
    task_id="load_data",
    python_callable=load_data,
    dag=dag
)

train_task = PythonOperator(
    task_id="train_model",
    python_callable=train_model,
    dag=dag
)

evaluate_task = PythonOperator(
    task_id="evaluate_model",
    python_callable=evaluate_model,
    dag=dag
)

load_task >> train_task >> evaluate_task
