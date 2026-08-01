select user_id, action, streak_length, start_date, end_date
from(
    select user_id, action, count(grp) as streak_length, 
    min(to_char(action_date,'YYYY-MM-DD')) as start_date, max(to_char(action_date,'YYYY-MM-DD')) as end_date,
    row_number() over (partition by user_id order by count(*) desc) as rnk 
    from(
        select user_id, 
        action_date, action_date - row_number() over(partition by user_id order by action_date) as grp,
        action
        from activity
    )
    group by user_id, grp, action
    having count(grp) >= 5
    order by streak_length desc, user_id
)where rnk = 1;