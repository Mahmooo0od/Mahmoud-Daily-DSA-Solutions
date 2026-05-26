select *
from (select U.name as results
      from MovieRating MR inner join Users U on U.user_id=MR.user_id
      group by U.name 
      order by count(rating) desc , U.name ASC) 
where ROWNUM=1 
union all 
select *
from (select M.title
      from MovieRating MR inner join Movies M on M.movie_id=MR.movie_id
      WHERE MR.created_at >= TO_DATE('2020-02-01', 'YYYY-MM-DD') 
      AND MR.created_at <= TO_DATE('2020-02-29', 'YYYY-MM-DD') 
      group by M.title
      order by avg(rating) desc ,M.title ASC) 
where ROWNUM=1


