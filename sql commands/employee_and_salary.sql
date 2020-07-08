use project2020;

select concat(e.fname,' ',e.lname) as fullname,  s.salary
from employees e, salary s
where s.employeeID = e.id;