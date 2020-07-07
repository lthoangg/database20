use Project2020;
DROP TABLE IF EXISTS MANAGER;
DROP TABLE IF EXISTS OPERATORS;
DROP TABLE IF EXISTS teachers;
drop table if exists students;
drop table if exists classes;
drop table if exists ASSESSMENT;
drop table if exists employees;
drop table if exists salary;

create table Operators(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    employeeID int not null,
    workShift varchar(12) not null
);
create table TEACHERS(
	id int not null primary key auto_increment,
    employeeID int not null, # reference to employees.id for me!
    quality varchar(45) not null,
    classID int not null
);
create table employees(
    id int not null primary key auto_increment,
    fname varchar(45) not null,
    lname VARCHAR(45) NOT NULL,
    address varchar(100) not null,
    age int not null
)
create table salary(
    id int not null primary key auto_increment,
    employeeID int, --referencetoEmployees.ID please
    salary int 
)
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
    timestart varchar(6) not null,
    timeend varchar(6) not null,
    teacherID int not null,
	fee int not null
);