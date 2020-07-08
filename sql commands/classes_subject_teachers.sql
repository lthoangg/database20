use project2020;

select cl.classname, s.name, concat(e.fname,' ',e.lname) as teachers_name
from classes cl, subjects s, employees e, teachers t
where cl.subjectID = s.id and cl.teacherID = e.id;