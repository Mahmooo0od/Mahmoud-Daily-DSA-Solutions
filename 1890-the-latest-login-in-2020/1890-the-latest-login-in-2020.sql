select user_id ,max(time_stamp) as last_stamp
from Logins 
where to_char(time_stamp,'YYYY') = '2020' 
group by user_id
