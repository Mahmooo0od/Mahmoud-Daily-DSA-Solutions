select U.name ,sum(nvl(amount,0)) as balance
from Users U left join Transactions T on U.account=T.account 
group by U.account , U.name 
having sum(amount)>10000