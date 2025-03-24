from airflow import DAG,Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime


def gerar_dados():
    hora = datetime.today().strftime("%Y-%m-%d %H:%M")

    with open(dataset.uri, "a+") as f:
        f.write(f'Atualização em {hora}')
        print("Atualizei")



caminho = '/home/milenafernandes/airflow/dados/raw/atualizacoes.txt'
dataset = Dataset(caminho)

with DAG(

    dag_id = "dag_produtora",
    catchup = False,
    start_date = datetime(2025,3,23),
    schedule_interval = "@hourly"

) as dag:
    escrever = PythonOperator(
    task_id = "escrever",
    python_callable = gerar_dados,
    outlets = [dataset]
    )
   
escrever
