from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime


def consumir_dados():

    with open(caminho, 'r') as f:
        print(f'{f.read()}')


caminho = '/home/milenafernandes/airflow/dados/raw/atualizacoes.txt'
dataset = Dataset(caminho)

with DAG(
    dag_id="dag_consumidora",
    catchup=False,
    start_date=datetime(2025, 3, 23),
    schedule = [dataset]
) as dag:
    
    ler = PythonOperator(
        task_id="ler",
        python_callable=consumir_dados,
        
    )

ler
