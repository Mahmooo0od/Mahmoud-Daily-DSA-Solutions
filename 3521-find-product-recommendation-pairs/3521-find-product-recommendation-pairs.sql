with UserProductPairs as (
    select pp.user_id, pp.product_id as product1_id, pp1.product_id as product2_id
    from ProductPurchases pp
    join ProductPurchases pp1
    on pp.user_id = pp1.user_id
    and pp.product_id < pp1.product_id
),
FrequentProductPairs as (
    select product1_id, product2_id, count(user_id) as customer_count
    from UserProductPairs
    group by product1_id, product2_id
    having count(user_id) >= 3
)
select 
p.product1_id, p.product2_id, pi.category as product1_category, pi2.category as product2_category,p.customer_count
from FrequentProductPairs p
join ProductInfo pi
on p.product1_id = pi.product_id
join ProductInfo pi2
on p.product2_id = pi2.product_id
order by p.customer_count desc, p.product1_id, p.product2_id