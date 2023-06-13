import boto3
session = boto3.Session(profile_name="573862076861_AdministratorAccess",region_name="us-east-1")
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='natalias-s3-bucket')

# 1. ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados
import csv

with open('movies.csv', encoding='utf-8') as movies_file:
    movies_reader = csv.reader(movies_file)
    movies_data = [row for row in movies_reader]

with open('series.csv', encoding='utf-8') as series_file:
    series_reader = csv.reader(series_file)
    series_data = [row for row in series_reader]


# 2. utilizar a lib boto3 para carregar os dados para a AWS
import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#3. acessar a AWS e grava no S3, no bucket definido com RAW Zone
import boto3
import os
from datetime import datetime

bucket_name = 'natalias-s3-bucket'
diretorio_no_bucket = 'caminho/para/diretorio'
arquivo_csv = '/caminho/para/arquivo.csv'
data_processamento = datetime.now().strftime('%Y%m%d') 
tipo_dado = 'filmes'
caminho_arquivo_origem = os.path.join('Local', 'CSV', tipo_dado, data_processamento, nome_arquivo)
caminho_arquivo_destino = os.path.join('Raw', caminho_arquivo_origem)

s3 = boto3.resource('s3')
#UPLOAD
s3.meta.client.upload_file(nome_arquivo, bucket_name, caminho_arquivo_destino)

