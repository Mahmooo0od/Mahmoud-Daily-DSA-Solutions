/* Write your PL/SQL query statement below */

Select Q.product_id , Q.first_year , Q.quantity ,  Q.price from (

Select product_id , year first_year ,quantity ,price , rank() over(partition by product_id order by year ) rn 
from Sales

) Q

where Q.rn = 1 