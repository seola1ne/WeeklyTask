create table Restaurant (
	id int not null auto_increment,
	name varchar(30) not null,
	address varchar(50) not null,
	phone varchar(16) not null,
	primary key(id)
);

create table Person (
	id int not null auto_increment,
	name varchar(30) not null,
	address varchar(50) not null,
	phone varchar(16) not null,
	primary key (id)
);

create table Reservation (
	id int not null auto_increment,
	restaurant_id int,
	person_id int,
	name varchar(50) not null,
	email varchar(30) not null,
	phone varchar(16) not null,
	num_guests int not null,
	date_time datetime not null,
	primary key (id),
	foreign key (restaurant_id) references Restaurant(id),
	foreign key (person_id) references Person(id)
);

insert into Person (name, address, phone) values ('원설아', '부산소마고', '010-1111-2222');

insert into Restaurant (name, address, phone) values ('김해시락국밥', '부산소마고 옆', '051-1111-2222');
insert into Restaurant (name, address, phone) values ('마산뼈해장국', '우리 집 옆', '055-2222-1111');