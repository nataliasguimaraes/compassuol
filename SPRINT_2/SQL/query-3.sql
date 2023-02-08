SELECT count(*) quantidade, editora.nome, cidade, estado 
FROM livro
JOIN editora on livro.editora = editora.codeditora
join endereco on editora.endereco = endereco.codendereco
GROUP by livro.editora, editora.nome, editora.endereco
order by quantidade desc
limit 5