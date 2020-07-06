use Project2020;
DROP TABLE IF EXISTS MANAGER;
DROP TABLE IF EXISTS OPERATORS;
DROP TABLE IF EXISTS teachers;
drop table if exists students;
drop table if exists classes;
drop table if exists ASSESSMENT;

create table Operators(
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
    age int not null,
    phonenumber varchar(10) not null,
    address varchar(100) not null,
    quality varchar(45) not null,
    classID int not null,
    wage int not null
);
create table STUDENTS(
	id int not null primary key auto_increment,
    fname varchar(45) not null,
    lname VARCHAR(45) NOT NULL,
    address varchar(100) not null,
    age int not null,
    classID int not null,
    result varchar(4)
);
create table CLASSES(
	id int not null primary key auto_increment,
    classname varchar(2) not null,
    subject varchar(15) not null,
    schedule varchar(12) not null,
    timestart time not null,
    timeend time not null,
    teacherID int not null,
	fee int not null
);