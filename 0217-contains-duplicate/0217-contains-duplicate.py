class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        set_1=set(nums) 

        return len(set_1)!=len(nums)
        