--Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV.
--Utilizar o caractere ; (ponto e vírgula) como separador.
--Lembre-se que o conteúdo do seu arquivo deverá respeitar
--a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:
-- CodLivro Titulo CodAutor NomeAutor Valor CodEditora NomeEditora


SELECT livro.cod as CodLivro, livro.titulo as Titulo, livro.cod as CodAutor, autor.nome as NomeAutor, valor as Valor, livro.editora as CodEditora, editora.nome as NomeEditora
FROM livro
JOIN autor on autor.codautor = livro.autor
JOIN editora on livro.editora = editora.codeditora 
GROUP BY livro.valor 
ORDER BY valor desc
LIMIT 10
