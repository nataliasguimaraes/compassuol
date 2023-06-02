import boto3
from botocore.exceptions import ClientError
from pyspark.sql import SparkSession

# Crie a sessão Spark
spark = SparkSession.builder.getOrCreate()

# Caminho da pasta contendo os arquivos JSON de entrada
json_folder = "s3://natalias-s3-bucket/Raw/Local/JSON/Movies/2023/05/09/"

# Nome do bucket de saída
output_bucket = "natalias-s3-bucket"
output_folder = "Trusted/Parquet/Movies/JSON/"

# Caminho de saída para os arquivos Parquet dentro do bucket
movies_parquet_path = f"{output_folder}movies.parquet"

# Leia os arquivos JSON com esquema automatico
movies_read = spark.read.json(json_folder, inferSchema=True)

# Escreva os dados como Parquet no bucket de saída dentro da pasta "trusted"
movies_read.coalesce(1).write.mode("overwrite").parquet(f"s3://{output_bucket}/{movies_parquet_path}")
