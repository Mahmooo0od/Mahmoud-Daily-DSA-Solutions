CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
   
    select distinct salary
      into result
      from (select salary
                 , dense_rank() over (order by salary desc) rn
              from Employee)
     where rn = n; 
     
        return result;
exception 
    when no_data_found then
        return null;
    
END;