select TO_CHAR(activity_date, 'YYYY-MM-DD') AS day , count(distinct user_id) as active_users
from Activity 
WHERE activity_date > DATE '2019-07-27' - 30 
  AND activity_date <= DATE '2019-07-27'
group by activity_date