select count(*) from companies where p_iscrizione is not null;
select count(distinct impresa) from categories where categoria is not null;
select count(distinct impresa) from cer_own_account;
select count(distinct impresa) from media_list;

select * from categories order by created desc limit 20 ;
select count(*) from impresas; 

delete from categories where categoria is null;

/*
select done, count(*) from impresas group by done
--update impresas set done = 0 
select * from companies

select * from impresas where done = 1 and impresa not in (select impresa from companies)

update impresas set done = 0 where done = 1 and impresa not in (select impresa from companies) 

update impresas set done = 1 where done = 0 and impresa in (select impresa from companies)

*/