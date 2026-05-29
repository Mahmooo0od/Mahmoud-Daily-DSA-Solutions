select NVL(E.employee_id,S.employee_id) as employee_id
from Employees E full outer join Salaries S on E.employee_id=S.employee_id 
where name is null OR salary is null 
order by employee_id