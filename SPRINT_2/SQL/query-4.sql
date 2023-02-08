select autor.nome, autor.codautor, autor.nascimento, count(livro.autor) quantidade
from livro 
right join autor on livro.autor = autor.codautor
group by autor.nome, autor.nascimento, autor.codautor
order by autor.nome asc
