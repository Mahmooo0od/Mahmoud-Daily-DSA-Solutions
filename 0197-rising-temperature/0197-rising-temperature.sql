select w1.id
from Weather w1 inner join weather w2 
on w1.recordDate=w2.recordDate+1
where w1.temperature >w2.temperature