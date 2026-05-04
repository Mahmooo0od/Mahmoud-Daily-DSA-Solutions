select P.product_id , NVL(ROUND(SUM(u.units * p.price) / NULLIF(SUM(u.units), 0), 2), 0) as average_price
from Prices P full outer join UnitsSold U 
on P.product_id=U.product_id AND U.purchase_date BETWEEN P.start_date AND P.end_date
group by P.product_id ;