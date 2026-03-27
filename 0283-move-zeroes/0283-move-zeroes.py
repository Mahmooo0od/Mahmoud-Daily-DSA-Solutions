class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0 
        right=0 
        for left in range(len(nums)) : 
            if nums[left]!=0 :
                nums[left],nums[right]=nums[right],nums[left] 
                right+=1 
        return nums
        