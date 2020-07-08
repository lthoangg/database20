use project2020;

insert into employees(fname,lname,address,age)
values('le','trong hoang','nowhere', 18);

update employees
set address = "where", age = 20
where fname="le" and lname="trong hoang" and id = 13;

select * from employees;