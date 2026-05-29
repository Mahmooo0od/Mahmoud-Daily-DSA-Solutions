select name , sum(nvl(distance,0)) as travelled_distance
from Users U left join Rides R on U.id=R.user_id
group by U.id ,name 
order by travelled_distance desc ,name asc 