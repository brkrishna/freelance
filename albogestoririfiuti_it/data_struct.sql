drop table if exists at_lines;
create table if not exists at_lines(
	section		varchar(100)	not null,
	id			int(11)			not null,
	name		varchar(255)	not null,
	add1		nvarchar(500)		null,
	add2		nvarchar(500)		null,
	cat			nvarchar(500)		null,
	regn		nvarchar(500)		null,
	d_n1		nvarchar(500)		null,
	d_n2		nvarchar(500)		null,
	d_n3		nvarchar(500)		null,
	d_n4		nvarchar(500)		null,
	ts 			timestamp 		NOT NULL DEFAULT CURRENT_TIMESTAMP,
	unique(section, name)
);

