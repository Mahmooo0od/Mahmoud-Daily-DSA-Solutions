with ranks as (
    select student_id, subject, exam_date, score, 
    dense_rank() over (partition by student_id, subject  order by exam_date) as first_rank,
    dense_rank() over (partition by student_id, subject  order by exam_date desc) as latest_rank
    from Scores
)
select f.student_id, f.subject, f.score as first_score, l.score as latest_score 
from ranks f
left join ranks l
    on f.student_id = l.student_id
    and f.subject = l.subject
where f.first_rank = 1
    and l.latest_rank = 1
    and l.score > f.score
order by 
    f.student_id, f.subject