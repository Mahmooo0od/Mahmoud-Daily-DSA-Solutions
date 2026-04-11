class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() 
        k=1
        maxx=1 
        Biggest=nums[0]
        for i in range(1,len(nums)): 
            if nums[i]==nums[i-1] : 
                k+=1 
                if k>maxx : 
                    maxx=k 
                    Biggest=nums[i]
            else : 
                k=1
        return Biggest 

        