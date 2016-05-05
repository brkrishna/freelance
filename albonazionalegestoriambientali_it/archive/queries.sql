select done, count(*) from impresas group by done
update impresas set done = 0

select count(*) from companies

select count(impresa) from companies

update impresas set done = 1 where impresa in (select impresa from companies) and done = 0


select * from companies order by impresa

select impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia from companies order by impresa