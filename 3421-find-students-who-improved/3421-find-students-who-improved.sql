WITH cte AS (
    SELECT DISTINCT 
        student_id, 
        subject, 
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject 
            ORDER BY exam_date 
        ) AS first_score, 
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject 
            ORDER BY exam_date desc
        ) AS latest_score
    FROM 
        Scores
)

SELECT 
    student_id,
    subject,
    first_score, 
    latest_score 
FROM 
    cte 
WHERE 
    latest_score > first_score
ORDER BY 
    student_id, 
    subject;