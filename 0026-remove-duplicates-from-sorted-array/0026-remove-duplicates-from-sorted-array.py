class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        i=0 
        J=1
        while J<len(nums) : 
            if nums[J]!=nums[i] : 
                 nums[i+1]=nums[J] 
                 i+=1 
            J+=1
        return i+1

        