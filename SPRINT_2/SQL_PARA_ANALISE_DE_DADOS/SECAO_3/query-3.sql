--3 Apresente a query para listar as 5 editoras com mais livros na biblioteca.
--O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
--Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

SELECT count(*) quantidade, editora.nome, cidade, estado 
FROM livro
JOIN editora on livro.editora = editora.codeditora
join endereco on editora.endereco = endereco.codendereco
GROUP by livro.editora, editora.nome, editora.endereco
order by quantidade desc
limit 5