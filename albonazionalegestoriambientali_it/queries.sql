select count(*) from companies;

select done, count(*) from impresas group by done;
select cat, count(*) from impresas group by cat;

select * from companies order by created desc limit 10;

delete from companies where p_iscrizione = null;

update impresas set done = 0 where done = 1 and impresa not in (select impresa from companies);