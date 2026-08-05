WITH top_performers AS (
  SELECT user_id
  FROM course_completions
  GROUP BY user_id
  HAVING COUNT(*) >= 5
     AND AVG(course_rating) >= 4
),
seq AS (
  SELECT
    c.user_id,
    c.course_name AS first_course,
    LEAD(c.course_name) OVER (
      PARTITION BY c.user_id
      ORDER BY c.completion_date, c.course_id
    ) AS second_course
  FROM course_completions c
  JOIN top_performers tp
    ON tp.user_id = c.user_id
),
agg AS (
  SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
  FROM seq
  WHERE second_course IS NOT NULL
  GROUP BY first_course, second_course
)
SELECT
  first_course   AS "first_course",
  second_course  AS "second_course",
  transition_count AS "transition_count"
FROM agg
ORDER BY
  transition_count DESC,
  LOWER(first_course),
  LOWER(second_course);