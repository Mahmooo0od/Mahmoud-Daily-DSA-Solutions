select TO_CHAR(activity_date, 'YYYY-MM-DD') AS day , count(distinct user_id) as active_users
from Activity 
WHERE activity_date > TO_DATE('2019-07-27', 'YYYY-MM-DD') - 30 
  AND activity_date <= TO_DATE('2019-07-27', 'YYYY-MM-DD')
group by activity_date