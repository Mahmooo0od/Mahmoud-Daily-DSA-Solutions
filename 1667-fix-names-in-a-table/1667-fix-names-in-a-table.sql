select user_id , substr(upper(name),1,1)||substr(lower(name),2) as name
from Users
order by user_id