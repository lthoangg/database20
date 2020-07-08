use project2020;

select e.id, concat(e.fname,' ',e.lname) as fullname, o.workShift
from employees e, operators o
where o.employeeID = e.id;