--update urls set done = 0 where done = 1 and source_cd in ('BH');

select distinct source_cd from reviews order by 1;

--delete from run_log;

--delete from reviews where source_cd = 'SH';

--update urls set done = 0 where done = 1 and source_cd = 'SB';

--update urls set url = 'http://zeenews.india.com/entertainment/reviews.htm' where source_cd = 'ZNI'

select * from reviews where source_cd = 'KM' order by name;

select source_cd, count(*) from reviews group by source_cd order by source_cd

delete from run_log;
delete from reviews;

drop view clean_names;
create view clean_names
as
select distinct trim(name) clean_name from reviews where source_cd in ('BS', 'IG', 'IN', 'MSN', 'NDTV', 'NR', 'PB')
order by name;

update reviews
set name = (select clean_name from clean_names, reviews where name like '%' || clean_name || '%')

delete from reviews_2;
insert into reviews_2  select source_cd, year, name, rvw_link, critic, rating, max_rtng, rvw_smy, director, actor1, actor2, actor3, genre, duration, ts from reviews;

update reviews
set name = (select clean_name from clean_names where name like '%' || clean_name || '%') 
where name in (  
select name
from clean_names, reviews
where name like '%' || clean_name || '%'
)
and source_cd = 'ZNI'

select source_cd, year, name, rvw_link from reviews order by name

update reviews_2
set director = (select director from movie_addl_data where clean_name = name),
actor1 = (select actor1 from movie_addl_data where clean_name = name),
actor2 = (select actor2 from movie_addl_data where clean_name = name),
actor3 = (select actor3 from movie_addl_data where clean_name = name)

drop view movie_addl_data;
create view movie_addl_data
as
select distinct trim(name) clean_name, director, actor1, actor2, actor3 
from reviews where source_cd in ('BWM', 'KM')
order by name;


select source_cd, name from reviews order by name

select name, source_cd from reviews order by name


drop table reviews;
create table reviews(
	source_cd	char(10) 		not null,
	year		integer 			null,
	name		varchar(500) 	not null,
	rvw_link 	varchar(1000) 	not null,
	critic		varchar(500) 		null,
	rating		real				null,
	max_rtng	real				null,
	rvw_smy		text				null,
	director	varchar(255)		null,
	actor1		varchar(255)		null,
	actor2		varchar(255)		null,
	actor3		varchar(255)		null,
	genre		varchar(255)		null,
	duration	varchar(10)			null,
	ts			timestamp default current_timestamp not null,
	unique(source_cd, year, rvw_link)	
);

select rvw_link, count(*)
from reviews
group by rvw_link
having count(*) > 1
order by rvw_link

select * from reviews where source_cd  = 'ZNI'