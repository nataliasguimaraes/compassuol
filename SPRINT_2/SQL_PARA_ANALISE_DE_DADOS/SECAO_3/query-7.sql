--7 Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.


select autor.nome
from livro 
full join autor on livro.autor = autor.codautor
where livro.autor is NULL 
group by autor.nome
order by autor asc
