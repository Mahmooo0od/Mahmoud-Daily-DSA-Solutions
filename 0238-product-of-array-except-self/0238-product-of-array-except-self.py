class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        x=1
        for i in range(1,n) :
            res[i]=nums[i-1]*x 
            x=res[i]
        x=1
        for i in range(n-2,-1,-1) :
            original=nums[i+1]*x
            res[i]=original*res[i]
            x=original
        return res
