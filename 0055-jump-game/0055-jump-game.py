class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goall = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goall:
                goall = i
        
        if goall==0 : 
            return True 
        else : 
            return False 