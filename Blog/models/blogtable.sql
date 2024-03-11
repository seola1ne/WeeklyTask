create table blog (
	id int(11) not null auto_increment,
	title varchar(45) null,
	content varchar(45) null,
	author varchar(45) null,
	create_at timestamp default current_timestamp() null,
	primary key(id)
);