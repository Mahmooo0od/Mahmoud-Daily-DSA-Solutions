select distinct T1.id , 
       case when T2.id is null and T1.p_id is not null then 'Leaf' 
            when T2.id is not null and T1.p_id is not null then 'Inner' 
            when T2.id is not null and T1.p_id is null then 'Root' 
            when T2.id is null and T1.p_id is null then 'Root' 
       End as "type"

from Tree T1 left join Tree T2 on T1.id=T2.p_id 
order by T1.id