class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Dict={}
        right_ac=0
        for J in range(len(nums)-1,-1,-1) :
            right_ac=right_ac+nums[J] 
            Dict[J]=right_ac-nums[J]
        left_ac=0
        for i in range(len(nums)): 
            if left_ac==Dict[i] :
                return i 
            left_ac+=nums[i]
        return -1 

