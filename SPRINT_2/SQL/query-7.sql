select autor.nome
from livro 
full join autor on livro.autor = autor.codautor
where livro.autor is NULL 
group by autor.nome
order by autor asc
