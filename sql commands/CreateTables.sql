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
  id int(11) NOT NULL,
  classname varchar(2) NOT NULL,
  subjectID int(15) NOT NULL,
  schedule varchar(12) NOT NULL,
  timestart varchar(6) NOT NULL,
  timeend varchar(6) NOT NULL,
  teacherID int(11) NOT NULL,
  fee int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE employees (
  id int(11) NOT NULL,
  fname varchar(45) NOT NULL,
  lname varchar(45) NOT NULL,
  address varchar(100) NOT NULL,
  age int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE operators (
  id int(11) NOT NULL,
  employeeID int(11) NOT NULL,
  workShift varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE result (
  id int(15) NOT NULL,
  studentid int(15) NOT NULL,
  result char(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE salary (
  id int(11) NOT NULL,
  employeeID int(11) NOT NULL,
  salary int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE students (
  id int(11) NOT NULL,
  fname varchar(45) NOT NULL,
  lname varchar(45) NOT NULL,
  address varchar(100) NOT NULL,
  age int(11) NOT NULL,
  classID int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `subject` (
  subjectid int(15) NOT NULL,
  name varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE teachers (
  id int(11) NOT NULL,
  employeeID int(11) NOT NULL,
  quality varchar(45) NOT NULL,
  classID int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE classes
  ADD PRIMARY KEY (id),
  ADD KEY teacherID (teacherID) USING BTREE,
  ADD KEY subjectID (subjectID);

ALTER TABLE employees
  ADD PRIMARY KEY (id);

ALTER TABLE operators
  ADD PRIMARY KEY (id),
  ADD KEY employeeID (employeeID);

ALTER TABLE result
  ADD PRIMARY KEY (id),
  ADD KEY id (studentid);

ALTER TABLE salary
  ADD PRIMARY KEY (id),
  ADD KEY employeeID (employeeID);

ALTER TABLE students
  ADD PRIMARY KEY (id),
  ADD KEY classID (classID) USING BTREE;

ALTER TABLE `subject`
  ADD KEY id (subjectid);

ALTER TABLE teachers
  ADD PRIMARY KEY (id),
  ADD KEY employeeID (employeeID);


ALTER TABLE classes
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE employees
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE operators
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE salary
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE students
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE teachers
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE classes
  ADD CONSTRAINT classes_ibfk_1 FOREIGN KEY (id) REFERENCES students (classID);

ALTER TABLE employees
  ADD CONSTRAINT employees_ibfk_1 FOREIGN KEY (id) REFERENCES teachers (employeeID),
  ADD CONSTRAINT employees_ibfk_2 FOREIGN KEY (id) REFERENCES operators (employeeID);

ALTER TABLE result
  ADD CONSTRAINT result_ibfk_1 FOREIGN KEY (studentid) REFERENCES students (id);

ALTER TABLE salary
  ADD CONSTRAINT salary_ibfk_1 FOREIGN KEY (employeeID) REFERENCES employees (id);

ALTER TABLE `subject`
  ADD CONSTRAINT subject_ibfk_1 FOREIGN KEY (subjectid) REFERENCES classes (subjectID);

ALTER TABLE teachers
  ADD CONSTRAINT teachers_ibfk_1 FOREIGN KEY (id) REFERENCES classes (teacherID);
COMMIT;