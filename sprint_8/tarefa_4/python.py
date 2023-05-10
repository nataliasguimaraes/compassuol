"""
1.Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv.
Carregue-o para dentro de um dataframe chamado df_nomes e,por fim, liste algumas linhas através do método show. Exemplo: df_nomes.show(5)
"""
from pyspark.sql import SparkSession

from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt")
df_nomes.show(5)



"""
2. Nesta etapa, será necessário adicionar código para renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.
"""
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)



"""
3. Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória:
Fundamental, Medio ou Superior.
"""
import random
from pyspark.sql.functions import rand, col, when
from pyspark.sql.types import IntegerType

df_nomes = df_nomes.withColumn("Escolaridade", when((rand() * 3).cast("int") == 0, "Fundamental")
                               .when((rand() * 3).cast("int") == 1, "Medio").otherwise("Superior"))
df_nomes.show(10)



"""
4. Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul,
de forma aleatória.
"""
df_nomes = df_nomes.withColumn("Pais", when((rand() * 13).cast("int") == 0, "Argentina")
                               .when((rand() * 13).cast("int") == 1, "Bolívia").when((rand() * 13).cast("int") == 2, "Brasil")
                               .when((rand() * 13).cast("int") == 3, "Chile").when((rand() * 13).cast("int") == 4, "Colômbia")
                               .when((rand() * 13).cast("int") == 5, "Equador").when((rand() * 13).cast("int") == 6, "Guiana")
                               .when((rand() * 13).cast("int") == 7, "Paraguai").when((rand() * 13).cast("int") == 8, "Peru")
                               .when((rand() * 13).cast("int") == 9, "Suriname").when((rand() * 13).cast("int") == 10, "Uruguai")
                               .when((rand() * 13).cast("int") == 11, "Venezuela").otherwise("Chile"))
df_nomes.show(10)



"""
5. Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010,
de forma aleatória. 
"""
from pyspark.sql.functions import lit, rand

df_nomes = df_nomes.withColumn("AnoNascimento", lit((rand() * (2010 - 1945) + 1945).cast("int")))
df_nomes.show(10)



"""
6. Usando o método select do dataframe (df_nomes), selecione as pessoas que nasceram neste século.
Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.
"""
df_select = df_nomes.filter((df_nomes["AnoNascimento"] >= 2000) & (df_nomes["AnoNascimento"] <= 2099)).select("Nomes")
df_select.show(10)



"""
7. Usando Spark SQL repita o processo da Pergunta 6.
Lembre-se que, para trabalharmos com SparkSQL, precisamos registrar uma tabela temporária e depois executar o comando SQL.
"""
df_nomes.createOrReplaceTempView ("pessoas")
spark.sql("SELECT Nomes FROM pessoas WHERE AnoNascimento BETWEEN 2000 AND 2099").show(10)



"""
8. Usando o método select do Dataframe df_nomes, Conte o número de pessoas que são da geração Millennials
(nascidos entre 1980 e 1994) no Dataset
"""
from pyspark.sql.functions import col

df_millennials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994))
count_millennials = df_millennials.count()

print("O número de pessoas da geração Millennials é:", count_millennials)



"""
9. Repita o processo da Pergunta 8 utilizando Spark SQL
"""
df_nomes.createOrReplaceTempView("pessoas")
count_millennials = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").first()[0]
print("O número de pessoas da geração Millennials é:", count_millennials)



"""
10. Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo.
Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade
- Baby Boomers – nascidos entre 1944 e 1964;
- Geração X – nascidos entre 1965 e 1979;4
- Millennials (Geração Y) – nascidos entre 1980 e 1994;
- Geração Z – nascidos entre 1995 e 2015.
"""
import pandas as pd

count_babyboomers = spark.sql("SELECT Pais, COUNT(*) as Quantidade, 'Baby Boomers' as Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1944 AND 1964 GROUP BY Pais")
count_geracaox = spark.sql("SELECT Pais, COUNT(*) as Quantidade, 'Geração X' as Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1965 AND 1979 GROUP BY Pais")
count_millennials = spark.sql("SELECT Pais, COUNT(*) as Quantidade, 'Millenials' as Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994 GROUP BY Pais")
count_geracaoz = spark.sql("SELECT Pais, COUNT(*) as Quantidade, 'Geração Z' as Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1995 AND 2015 GROUP BY Pais")

df_geracoes = count_babyboomers.union(count_geracaox).union(count_millennials).union(count_geracaoz)
df_geracoes = df_geracoes.orderBy(['Pais','Geracao','Quantidade'])

df_geracoes_pd = df_geracoes.toPandas()
print(df_geracoes_pd)
