class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        i=0 
        for J in range(1,len(nums)) : 
            if nums[J]!=nums[i] : 
                 nums[i+1]=nums[J] 
                 i+=1 
        return i+1

        