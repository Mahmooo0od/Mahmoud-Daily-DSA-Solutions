select distinct num as ConsecutiveNums
from (select id , num ,lag(num) over(order by id) as LG ,lead(num) over(order by id) as LD
from Logs)
where num=LG and num=LD