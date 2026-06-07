select round(score,2) as score ,Dense_rank() over (order by score desc ) as rank
from Scores 
order by 1 desc 