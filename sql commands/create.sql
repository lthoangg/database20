drop schema if EXISTS project2020;
create schema project2020;

use Project2020;
DROP TABLE IF EXISTS MANAGER;
DROP TABLE IF EXISTS OPERATORS;
DROP TABLE IF EXISTS teachers;
drop table if exists students;
drop table if exists classes;
drop table if exists ASSESSMENT;
drop table if exists employees;
drop table if exists salary;

CREATE TABLE classes (
    id INT,
    classname VARCHAR(2),
    subjectID INT,
    schedule VARCHAR(12),
    timestart VARCHAR(6),
    timeend VARCHAR(6),
    teacherID INT,
    fee INT
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(45),
    lname VARCHAR(45),
    address VARCHAR(100),
    age INT
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE operators (
    id INT,
    employeeID INT,
    workShift VARCHAR(12)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE result (
    id INT,
    studentid INT,
    result CHAR(4)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE salary (
    id INT,
    employeeID INT,
    salary INT
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE students (
    id INT,
    fname VARCHAR(45),
    lname VARCHAR(45),
    address VARCHAR(100),
    age INT,
    classID INT
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE subjects (
    id INT,
    name varchar(5)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE teachers (
    id INT,
    employeeID INT,
    quality VARCHAR(45),
    classID INT
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

ALTER TABLE classes
  ADD PRIMARY KEY (id);

ALTER TABLE operators
  ADD PRIMARY KEY (id);

ALTER TABLE result
  ADD PRIMARY KEY (id);

ALTER TABLE salary
  ADD PRIMARY KEY (id);

ALTER TABLE students
  ADD PRIMARY KEY (id);

ALTER TABLE subjects
  ADD PRIMARY KEY (id);

ALTER TABLE teachers
  ADD PRIMARY KEY (id);

ALTER TABLE classes
  MODIFY id int NOT NULL AUTO_INCREMENT;
  
ALTER TABLE subjects
  MODIFY id int NOT NULL AUTO_INCREMENT;
  
ALTER TABLE employees
  MODIFY id int NOT NULL AUTO_INCREMENT;

ALTER TABLE operators
  MODIFY id int NOT NULL AUTO_INCREMENT;

ALTER TABLE salary
  MODIFY id int NOT NULL AUTO_INCREMENT;

ALTER TABLE students
  MODIFY id int NOT NULL AUTO_INCREMENT;

ALTER TABLE teachers
  MODIFY id int NOT NULL AUTO_INCREMENT;

ALTER TABLE result
  MODIFY id int NOT NULL AUTO_INCREMENT;

COMMIT;