drop table if exists impresas;
create table if not exists impresas(
	impresa	varchar(255) not null primary key,
	created timestamp not null default current_timestamp
);

drop table if exists companies;
create table if not exists companies(
	impresa	varchar(255) not null primary key,
	p_iscrizione varchar(2),
	n_iscrizione varchar(25),
	denominazione varchar(255),
	codicefiscale varchar(255),
	via varchar(255),
	cap varchar(10),
	comune varchar(100),
	sigla_provincia varchar(2),
	created timestamp not null default current_timestamp
);

drop table if exists categories;
create table if not exists categories(
	impresa	varchar(255) not null,
	categoria varchar(255), 
	tipo_iscrizione varchar(255), 
	classe varchar(255), 
	stato varchar(255), 
	causale_sospensione varchar(255), 
	sospesa_dal varchar(255), 
	sospesa_fino_al varchar(255), 
	inizio varchar(255), 
	data_scadenza varchar(255), 
	sotto_categoria	varchar(255),
	created timestamp not null default current_timestamp
);

drop table if exists cer_own_account;
create table if not exists cer_own_account(
	impresa	varchar(255) not null,
	codice varchar(50),
	descrizione varchar(1000),
	created timestamp not null default current_timestamp
);

drop table if exists media_list;
create table if not exists media_list(
	impresa	varchar(255) not null,
	targa varchar(255),
	tipo_mezzo varchar(255),
	catg_attive varchar(255),
	created timestamp not null default current_timestamp
);	

create index impresas_done on impresas(done);
create index impresas_cat on impresas(cat);
create index impresas_cer on impresas(cer);
create index impresas_media_list on impresas(media_list);
