# SPRINT#2: SQL E CONCEITOS USADOS NA ÁREA DE DADOS

<p align="right">
Realizada entre 01/02/23 e 14/02/23<br>
Monitor Antonio Alex de Souza
</p>

<!------------------------------------SUMMARY-->
<p align="center">
<a href="https://github.com/nataliasguimaraes/compassuol/main/sprint_02/README.md#rocket-stacks--tools">STACKS & TOOLS</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/nataliasguimaraes/compassuol/main/sprint_02/README.md#-pontos-abordados">PONTOS ABORDADOS</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/nataliasguimaraes/compassuol/main/sprint_02/README.md#-anota%C3%A7%C3%B5es-pessoais">ANOTAÇÕES PESSOAIS</a>&nbsp;&nbsp;&nbsp;

#

 <!------------------------------------STACKS-->
#### :rocket: STACKS & TOOLS:
<p align="left">
  <a href="https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/GitHub"><img  alt="GIT"  width="30" height="30" src="https://user-images.githubusercontent.com/104440384/218911437-22204b9b-b55c-4bdd-8e0e-ac539c3c3627.png"><a/>
  <a href="https://code.visualstudio.com/"><img  alt="Vscode"  width="30" height="30" src="https://user-images.githubusercontent.com/59892368/149663512-3f83da57-bdfe-4cef-bcc2-feb304a738ff.png"><a/>
 <a href="https://developer.mozilla.org/en-US/docs/Glossary/SQL"><img  alt="SQL"  width="30" height="30" src="https://user-images.githubusercontent.com/104440384/218635686-f8b56c01-19dd-451e-b787-4ab7d2e9fed2.png"><a/>
 <a href="https://www.pgadmin.org/faq/"><img  alt="PGAdmin"  width="30" height="30" src="https://user-images.githubusercontent.com/104440384/218912256-3200c7d3-0819-4d44-a012-f6177f113c25.png"><a/>
 <a href="https://dbeaver.io/about/"><img  alt="DBeaver"  width="30" height="30" src="https://user-images.githubusercontent.com/104440384/218912441-645f23ca-b235-49e2-89eb-0340aa2f10ff.png"><a/>
 <a href="https://www.sqlite.org/about.html"><img  alt="SQlite"  width="30" height="30" src="https://user-images.githubusercontent.com/104440384/218912701-704fbb55-eb7d-4913-b3bc-69e8feacd840.png"><a/>      
 <a href="https://www.oracle.com/br/big-data/what-is-big-data/"><img  alt="BigData"  width="30" height="30" src="https://user-images.githubusercontent.com/104440384/218922251-ad64d2e3-ec92-42c4-b891-858bf6ff8c47.png"><a/>   
<br>
 
  #
<!------------------------------------PRODUCTION SKILLS-->

#### 📚 PONTOS ABORDADOS:

* SQL PARA ANÁLISE DE DADOS
  * [`criação e maninupação de tabelas`](https://www.w3schools.com/sql/sql_create_table.asp) criar e editar tabelas no database;
  * [`sintaxes de consultas`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#select-syntax) como select, from, where, group by, having, order by, limit;
  * [`operadores aritméticos`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#arithmeticoperators) para executar operações matemáticas;
  * [`operadores de comparação`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#comparisonfunctions) para comparar dois valores retornando 'true' or 'false';
  * [`operadores lógicos`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#logicfunctions) como and, or, not, betwen, like, ilie, is null para unir operações simples em uma composta;
  * [`operações de conversão`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#syntax-casting) para  definir como os itens flexíveis são colocados no contêiner;
  * [`funções agregadas`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#functions) como count, sum, min, max, avg para executar operações aritméticas nos registros de uma coluna;
  * [`joins`](https://cloud.google.com/bigquery/docs/reference/legacy-sql?hl=pt-br#joins) para relacionar múltiplas tabelas;
  * [`unions`](https://www.w3schools.com/sql/sql_union.asp) para combinar o resultado de dois ou mais selects;
  * [`subqueries`](https://www.devmedia.com.br/trabalhando-com-subqueries/40134) para consultar dados de outras consultas;
 <br>  Dentre outros...
   
* BIG DATA FUNDAMENTOS 3.0
  * [`definição`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#9e71d883d97941a1a5ab0ae92941de8e)
  * [`sistemas de armazenamento`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#82ec797427da43868a5cd4d123d015fd) tipos de armazenamento, acesso e definição do produto;
  * [`armazenamento e espaço paralelo`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#79890d860d1446e6a40e254ed72d2160) cluster, armazenamento em nuvem, softwares;
  * [`cloud computing`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#a24af6e1235e456a8189d53fb502909a) provedores em nuvem, AWS;
  * [`mlops e dataops`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#77551ff4b32643088abe556eefe4123e) machine learning, fluxo de trabalho, linha de produção de analytics, ferramentas;
  * [`daas`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#7401a8522c614b3986c0ad18e0b1a2e3) dados como serviços, arquitetura DaaS, data mesh;
  * [`etl`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#f1d9fd0f264d4fa195d0c6494b3b72b5) extração, trasnformação e carga de dados;
  * [`projeto big data`](https://www.notion.so/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778?pvs=4#fa09b3974d4f4a1ca603048759ffc8ae) casos de uso, business case, planejamento, total business value assessment;
 <br>  Dentre outros...

#
<!------------------------------------ANOTAÇÕES-->
#### 📝 ANOTAÇÕES PESSOAIS:

   * SQL: Caderno físico. 
   * <a href="https://natycodes.notion.site/Big-Data-Fundamentos-7a17f60c229e429fa86a55e31cc46778">NOTION: BANCO DE DADOS</a>

 <br>  
   
<hr>
   
[![Email](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guimaraessnatalia@gmail.com)
[![Linkedin](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/natalia-guimar%C3%A3es-6a357721b)
   
![CompassUOL](https://user-images.githubusercontent.com/104440384/214567499-2dc24c5e-d882-4825-b953-f5a69a6be44e.jpg)
