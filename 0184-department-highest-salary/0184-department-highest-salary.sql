select Department , Employee , salary
from ( select D.name as Department ,E.name as Employee , E.salary as salary , 
           Dense_Rank() over(partition by E.departmentId order by E.salary desc) as RN
       from Employee E inner join Department D on E.departmentId=D.id )
where RN=1