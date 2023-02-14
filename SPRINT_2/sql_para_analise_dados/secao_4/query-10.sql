--10 A comissão de um vendedor é definida a partir de um percentual
--sobre o total de vendas (quantidade * valor unitário) por ele realizado.
--O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor.
--Com base em tais informações, calcule a comissão de todos os vendedores,
--considerando todas as vendas armazenadas na base de dados com status concluído.
--As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao.
--O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.


select nmvdd as vendedor, SUM(qtd*vrunt) as valor_total_vendas, (round(perccomissao*SUM(qtd*vrunt)/100,2)) as comissao
from tbvendas 
join tbvendedor using(cdvdd)
where status ='Concluído' 
group by nmvdd
order by comissao desc