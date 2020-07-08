use project2020;

select concat(std.fname,' ',std.lname) AS fullname, r.result
from students std, result r
where std.id = r.studentid;