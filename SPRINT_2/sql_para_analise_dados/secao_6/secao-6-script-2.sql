--Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV.
--Utilizar o caractere | (pipe) como separador.
--Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:
-- CodEditora NomeEditora QuantidadeLivros


SELECT editora.codeditora as CodEditora, editora.nome as NomeEditora, count(*) QuantidadeLivros
FROM livro
JOIN editora on livro.editora = editora.codeditora
GROUP by livro.editora, editora.nome
ORDER by QuantidadeLivros desc
LIMIT 5

