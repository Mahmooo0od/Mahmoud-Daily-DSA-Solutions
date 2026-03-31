class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        J=0 
        i=0 
        dis=0 
        maxx=dis 
        ks=0
        while J<len(nums) : 
            if nums[J]==0 and ks==1 : 
                while nums[i]==1 : 
                    i+=1 
                i+=1 
            elif nums[J]==0 and ks==0 : 
                ks=1 
            dis=J-i 
            if dis>maxx : 
                maxx=dis 
            J+=1
        return  maxx 
            