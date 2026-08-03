;with cte_base as (  --join student with sessions to get required fields and get previous and next session dates
    select ss.session_id, ss.student_id, s.student_name, s.major, subject, session_date, ss.hours_studied,
           coalesce(lag(ss.session_date) over (partition by ss.student_id order by session_date), session_date) prev_session_date,    
           coalesce(lead(ss.session_date) over (partition by ss.student_id order by session_date), session_date) next_session_date
    from study_sessions ss
    join students s
      on ss.student_id = s.student_id 
),

cte_sessions as ( --filter out data where student's sessions are more then 2 days apart and calculate total study hours from remaining sessions
    select session_id, student_id, student_name, major, subject, session_date, sum(hours_studied) over (partition by student_id order by (select null)) as total_study_hours
    from cte_base
    where datediff(day, prev_session_date, session_date) <= 2 
      and datediff(day, session_date, next_session_date) <= 2     
),

cte_cycles as ( --get number of sessions for each sudent along with sesison cycles based on subjects
    select *,
           row_number() over (partition by student_id, subject order by session_date) cycles,
           row_number() over (partition by student_id order by session_date) total_length          
    from cte_sessions
),

cte_agg_cycles as ( --make sure student has 1 unque cycle (is it possible to have 2+ unique?)
    select student_id, count(1) as unique_cycles from (
        select distinct student_id,
               string_agg(subject, ',')  within group (order by total_length ASC) as cycle_desc
        from cte_cycles
        group by student_id, cycles
    ) x
    group by student_id
    having count(1) = 1

)

select student_id, student_name, major, (total_length / cycles) as cycle_length, total_study_hours from (
    select student_id, student_name, major,  max(total_length) as total_length, max(cycles) as cycles, total_study_hours
    from cte_cycles
    group by student_id, student_name, major, total_study_hours   
) get_max_cycles
where cycles > 1                   --to make sure at least 2 cycles
  and total_length / cycles >= 3   --to make sure at least 3 cycles were completed
  and total_length % cycles = 0    --to make sure student completed subject cycles
  and student_id in (select student_id from cte_agg_cycles)    --to make sure all cycles for student match
order by cycle_length desc, total_study_hours desc