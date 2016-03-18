--processed boolean not null default 0 check(processed IN(0,1))

drop table urls;
create table urls(
	source_cd	char(10)		not null,
	source 		varchar(100) 	not null,
	url 		varchar(1000)	not null,
	ts 			timestamp default current_timestamp not null,
	done 		boolean 		not null default 0 check(done in(0,1)),
	unique(source_cd)
);

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

drop table run_log;
create table run_log(
	source_cd	char(10)	not null,
	started		timestamp default current_timestamp not null,
	completed	timestamp 			null,
	unique(source_cd, started)
	
);

drop view clean_names;
create view clean_names
as
select distinct trim(name) clean_name from reviews where source_cd in ('BS', 'IG', 'IN', 'MSN', 'NDTV', 'NR', 'PB')
order by name;

drop view movie_addl_data;
create view movie_addl_data
as
select distinct trim(name) clean_name, director, actor1, actor2, actor3 
from reviews where source_cd in ('BWM', 'KM')
order by name;

delete from urls;
insert into urls (source_cd, source, url) values ('BH','Bhaskar', 'http://bollywood.bhaskar.com/reviews/movie-reviews/');
insert into urls (source_cd, source, url) values ('BL','BollywoodLife', 'http://www.bollywoodlife.com/reviews');
insert into urls (source_cd, source, url) values ('BM','BollywoodMantra', 'http://www.bollywoodmantra.com/');
insert into urls (source_cd, source, url) values ('BOS','BollySpice', 'http://bollyspice.com/category/reviews');
insert into urls (source_cd, source, url) values ('BS','Bharat Student', 'http://www.bharatstudent.com/cafebharat/movie_reviews-Hindi-Movie-Reviews-1.php');
insert into urls (source_cd, source, url) values ('BW','Bollywood.Com', 'http://www.bollywood.com/');
insert into urls (source_cd, source, url) values ('BW3','Bollywood3', 'http://www.bollywood3.com/');
insert into urls (source_cd, source, url) values ('BWH','Bollywood Hungama', 'http://www.bollywoodhungama.com/movies/reviews/');
insert into urls (source_cd, source, url) values ('BWM','Bollywood Mixer', 'http://bollywoodmixer.com/');
insert into urls (source_cd, source, url) values ('DNAI','DNA India', 'http://www.dnaindia.com/film-reviews');
insert into urls (source_cd, source, url) values ('ETC','ETC', 'http://www.etc.in/reviews/read.html?id=8372');
insert into urls (source_cd, source, url) values ('FF','Filmfare', 'http://www.filmfare.com/reviews');
insert into urls (source_cd, source, url) values ('FP','First Post', 'http://www.firstpost.com/bollywood/mahabharat-review-made-for-dummies-by-dummies-1309337.html');
insert into urls (source_cd, source, url) values ('FS','FailSuccess', 'http://failsuccess.com/category/masala-news/reviews/');
insert into urls (source_cd, source, url) values ('GS','Glam Sham', 'http://www.glamsham.com/movies/reviews/');
insert into urls (source_cd, source, url) values ('HT','Hindustan Times', 'http://www.hindustantimes.com/entertainment/reviews/movie-review-by-sarit-ray-mahabharat-far-from-epic/article1-1167058.aspx');
insert into urls (source_cd, source, url) values ('IBN','IBN', 'http://ibnlive.in.com/movies/reviews/masands_verdict/');
insert into urls (source_cd, source, url) values ('IE','Indian Express', 'http://indianexpress.com/section/entertainment/movie-review/');
insert into urls (source_cd, source, url) values ('IG','India Glitz', 'http://www.indiaglitz.com/channels/hindi/reviews.asp');
insert into urls (source_cd, source, url) values ('IN','Indicine', 'http://www.indicine.com/in/bollywood/reviews-bollywood/');
insert into urls (source_cd, source, url) values ('IT','India Today', 'http://indiatoday.intoday.in/story/mahabharat-movie-review/1/333288.html');
insert into urls (source_cd, source, url) values ('KM','Koi Moi', 'http://www.koimoi.com/category/reviews/');
insert into urls (source_cd, source, url) values ('KR','KomalsReviews', 'http://komalsreviews.wordpress.com/');
insert into urls (source_cd, source, url) values ('MD','Mid-Day', 'http://www.mid-day.com/entertainment/2013/dec/271213-movie-review-mahabharat-3d.htm');
insert into urls (source_cd, source, url) values ('MM','Mumbai Mirror', 'http://www.mumbaimirror.com/entertainment/bollywood/Film-review-Nostalgia-animated/articleshow/28021066.cms');
insert into urls (source_cd, source, url) values ('MSN','MSN India', 'http://movies.in.msn.com/reviews/');
insert into urls (source_cd, source, url) values ('MZ','MovieZadda', 'http://www.moviezadda.com/movies/movie-reviews');
insert into urls (source_cd, source, url) values ('NDTV','NDTV', 'http://movies.ndtv.com/movie-reviews/mahabharat-3d-animation-movie-review-909');
insert into urls (source_cd, source, url) values ('NR','Nowrunning', 'http://www.nowrunning.com/movie/reviews/');
insert into urls (source_cd, source, url) values ('OI','OneIndia', 'http://entertainment.oneindia.in/bollywood/reviews/');
insert into urls (source_cd, source, url) values ('PB','Planet Bollywood', 'http://www.planetbollywood.com/displayReviewIndex.php?scid=7');
insert into urls (source_cd, source, url) values ('RE','Reuters', 'http://in.reuters.com/news/entertainment/bollywood');
insert into urls (source_cd, source, url) values ('REDIFF','REDIFF', 'http://www.rediff.com/movies/report/review-mahabharat-dumbed-down/20131227.htm');
insert into urls (source_cd, source, url) values ('RM','Rajeev Masand', 'http://www.rajeevmasand.com/');
insert into urls (source_cd, source, url) values ('RMH','RateMoviesHere', 'http://www.ratemovieshere.com/');
insert into urls (source_cd, source, url) values ('SB','Santa Banta', 'http://www.santabanta.com/cinema.asp?catname=movie%20review');
insert into urls (source_cd, source, url) values ('SH','Smashits', 'http://www.smashits.com/news/movie-reviews-1.html');
insert into urls (source_cd, source, url) values ('SIFY','Sify', 'http://www.sify.com/movies/mahabharat-review-a-great-tale-diluted-review-bollywood-15046035.html');
insert into urls (source_cd, source, url) values ('SULEKHA','Sulekha', 'http://movies.sulekha.com/hindi//default.htm');
insert into urls (source_cd, source, url) values ('TOI','Times of India', 'http://timesofindia.indiatimes.com/entertainment/movie-reviews');
insert into urls (source_cd, source, url) values ('YAHOO','Yahoo India', 'http://in.movies.yahoo.com/blogs/movie-reviews/yahoo-movies-review-dhoom-3-113327588.html');
insert into urls (source_cd, source, url) values ('ZNI','Zee News India', 'http://zeenews.india.com/entertainment/bollywood.htm');
