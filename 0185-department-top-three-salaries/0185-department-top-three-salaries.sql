with abc as(
    select a.name as department , b.name as employee , b.salary , dense_rank() over(partition by b.departmentid order by b.salary desc)  as rn from employee b left join 
    department a on a.id = b.departmentid
)
select department , employee, salary from abc 
where rn<=3;