select distinct P.product_id , product_name
from Product P inner join Sales S on P.product_id=S.product_id 
where sale_date >= '2019-01-01' and sale_date<= '2019-03-31' and P.product_id not in (
                                                select distinct Se.product_id 
                                                from Sales Se
                                                where Se.sale_date<'2019-01-01' or Se.sale_date>'2019-03-31'
)