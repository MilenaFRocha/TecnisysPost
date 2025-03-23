# Prática da aula com BranchOperator para praticar
# Essa DAG lê os arquivos que estão na pasta se existir e os separa em pastas de suas extensões, movendo-os
# Caso não haja nenhum arquivo, task skippada
# Próximo passo é ativar essa DAG sempre que um novo arquivo entrar

import os
import shutil
from airflow import DAG
from airflow.decorators import task, task_group
from airflow.utils.dates import days_ago
from datetime import datetime

DATA_RAW = '/home/milenafernandes/airflow/dados/raw'
DATA_PROCESSED = '/home/milenafernandes/airflow/dados/processed'

with DAG(
    dag_id='Processa_arquivos_por_extensao',
    start_date=datetime(2025, 3, 22),
    schedule_interval='@hourly',
    catchup=False
) as dag:


    @task.branch
    def verifica_arquivo_para_processar(path_raw, path_processed):
        if os.path.exists(path_raw) and os.path.exists(path_processed):
            arquivos = os.listdir(path_raw)
            if arquivos:
                print(f'Arquivos a serem processados: {arquivos}')
                return 'separa_extensao'  # Nome da próxima task se houver arquivo
            else:
                print('Não existe arquivos a serem processados na pasta raw')
                return 'sem_arquivos'  
        else:
            if not os.path.exists(path_raw):
                print(f'O caminho raw não existe: {path_raw}')
            if not os.path.exists(path_processed):
                print(f'O caminho processed não existe: {path_processed}')
            return 'sem_arquivos'

   
    def pega_extensao(nome_arquivo):
        return os.path.splitext(nome_arquivo)[1].strip('.') 


    @task
    def separa_extensao():
        arquivos = os.listdir(DATA_RAW)
        for arquivo in arquivos:
            extensao = pega_extensao(arquivo)
            pasta_destino = os.path.join(DATA_PROCESSED, extensao)
            os.makedirs(pasta_destino, exist_ok=True)

            origem = os.path.join(DATA_RAW, arquivo)
            destino = os.path.join(pasta_destino, arquivo)

            try:
                shutil.move(origem, destino)
                print(f'Arquivo {arquivo} movido para {destino}')
            except Exception as e:
                print(f'Erro ao mover o arquivo {arquivo}: {e}')


    @task
    def sem_arquivos():
        print('Nenhum arquivo encontrado ou caminho inválido.')

    
    decisao = verifica_arquivo_para_processar(DATA_RAW, DATA_PROCESSED)
    separa_extensao_task = separa_extensao()
    sem_arquivos_task = sem_arquivos()

  
    decisao >> [separa_extensao_task, sem_arquivos_task]
