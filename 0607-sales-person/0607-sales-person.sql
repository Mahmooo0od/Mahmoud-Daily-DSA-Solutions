select name
from SalesPerson 
where sales_id not in (select distinct sales_id
                       from Orders O , Company C
                       where O.com_id=C.com_id and C.name='RED')