
SELECT TO_CHAR(sell_date) AS "sell_date", 
COUNT(DISTINCT(product)) AS "num_sold",
LISTAGG(product, ',') WITHIN GROUP (ORDER BY product) AS "products"
FROM (select distinct * from Activities) 
GROUP BY sell_date 
ORDER BY sell_date;