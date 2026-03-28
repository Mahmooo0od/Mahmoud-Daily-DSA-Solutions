class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=0 
        i=0 
        J=len(nums)-1
        nums.sort()
        while i<J : 
            if nums[i]+nums[J]==k : 
                c+=1 
                i+=1 
                J-=1 
            elif nums[i]+nums[J]>k : 
                J-=1  
            else : 
                i+=1 
        return c