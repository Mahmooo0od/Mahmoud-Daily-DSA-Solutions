select E.name as Employee
from Employee E inner join Employee M on M.id=E.managerId
where E.salary>M.salary