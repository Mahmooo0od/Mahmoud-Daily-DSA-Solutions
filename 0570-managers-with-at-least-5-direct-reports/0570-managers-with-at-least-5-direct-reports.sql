select M.name as name
from Employee E,Employee M 
where E.managerId=M.id
group by M.id,M.name
having count(E.id)>=5