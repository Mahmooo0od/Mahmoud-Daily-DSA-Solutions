class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        J=0 
        i=0 
        sums=0 
        maxx=sums 
        ks=k
        for J in range(len(nums)) : 
            if nums[J]==0 : 
                ks-=1 

            while ks< 0 : 
                if nums[i]==0 :  
                    ks+=1  
                i+=1
            sums=(J-i)+1 
            if sums>maxx : 
                maxx=sums 
        return maxx
