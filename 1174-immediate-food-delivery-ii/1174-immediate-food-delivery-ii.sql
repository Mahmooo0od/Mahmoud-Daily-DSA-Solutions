with cte as (select *
             from( select delivery_id ,
                          customer_id ,
                          order_date ,
                          customer_pref_delivery_date ,
                       Rank() over (partition by customer_id order by order_date ) as Rn

              from Delivery )
              where RN=1 )


select round(count( distinct case when order_date = customer_pref_delivery_date then customer_id end ) /
        count(distinct customer_id)*100,2) as immediate_percentage

from cte 

