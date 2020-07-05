use Project2020;

create table MANAGER(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fname varchar(45) not null,
    lname VARCHAR(45) NOT NULL,
    phonenumber varchar(10) not null,
    address varchar(45) not null
);
create table TEACHERS(
	id int not null primary key auto_increment,
    fname varchar(45) not null,
    lname VARCHAR(45) NOT NULL,
    age int,
    phonenumber varchar(10) not null,
    address varchar(2) not null,
    quality varchar(45),
    classname varchar(45) not null
);
create table STUDENTS(
	id int not null primary key auto_increment,
    fname varchar(45) not null,
    lname VARCHAR(45) NOT NULL,
    age int not null,
    classname varchar(45) not null,
    result varchar(100)
);
create table CLASSES(
	id int not null primary key auto_increment,
    name varchar(45) not null,
    subject varchar(15) not null,
    teachername varchar(45) not null,
    day varchar(12) not null,
    timestart time not null,
    timeend time not null,
	fee int not null
);
create table ASSESSMENT(
	id int not null primary key auto_increment,
    date datetime,
    studentname varchar(45),
    comment varchar(100),
    result varchar(4)
);