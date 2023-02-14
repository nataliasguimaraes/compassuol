--12 Apresente a query para listar código, nome e data de nascimento dos dependentes
--do vendedor com menor valor total bruto em vendas (não sendo zero).
--As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

select cddep, nmdep, dtnasc, sum(qtd*vrunt) as valor_total_vendas
from tbvendedor
left join tbvendas on tbvendas.cdvdd = tbvendedor.cdvdd 
join tbdependente on tbvendedor.cdvdd = tbdependente.cdvdd
where status = 'Concluído'
group by tbvendas.cdvdd
order by valor_total_vendas ASC 
limit 1