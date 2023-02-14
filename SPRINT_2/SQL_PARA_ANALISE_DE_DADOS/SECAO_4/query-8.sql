--8 Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem),
--e que estas vendas estejam com o status concluída. 
--As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

with cdvdd as (select cdvdd, count(*))
select cdvdd, nmvdd
from tbvendas
join tbvendedor using(cdvdd)
where status ='Concluído' 
group by cdvdd
order by COUNT(*) DESC
limit 1



















