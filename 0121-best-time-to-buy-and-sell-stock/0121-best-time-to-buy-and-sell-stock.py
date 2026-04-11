class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k=0 
        maxx=0 
        i=0
        for J in range(len(prices)) : 
            if prices[J]>=prices[i] : 
                k=prices[J]-prices[i] 
                if k>maxx :
                    maxx=k 
                J+=1 
            else : 
                i=J 
        return maxx