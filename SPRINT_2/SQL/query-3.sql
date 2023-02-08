SELECT count(*) quantidade, t2.nome, t3.cidade, t3.estado 
FROM livro t1
JOIN editora t2 on (t1.editora = t2.codeditora)
join endereco t3 on (t2.endereco = t3.codendereco)
GROUP by t1.editora, t2.nome, t2.endereco
order by quantidade desc
limit 5