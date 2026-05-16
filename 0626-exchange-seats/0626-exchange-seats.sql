select id - 1 as id, student from Seat where mod(id, 2)  = 0
union all
select id as id, student from Seat where id = (select max(id) from Seat) and mod(id, 2) = 1
union all
select id + 1 as id, student from Seat where mod(id, 2) = 1 and id <> (select max(id) from Seat) 
order by id 