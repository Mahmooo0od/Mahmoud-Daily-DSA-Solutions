select contest_id ,round(count(user_id)/(SELECT COUNT(*) FROM Users)*100,2) as percentage
from Register
group by contest_id 
order by percentage desc , contest_id asc