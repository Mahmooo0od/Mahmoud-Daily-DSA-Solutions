select user_id as buyer_id  , to_char(join_date,'YYYY-MM-DD') as join_date,NVL(count(order_id),0)  as orders_in_2019
from Users U left join Orders O on U.user_id=O.buyer_id AND EXTRACT(YEAR FROM O.order_date) = 2019
group by user_id , join_date 
order by user_id