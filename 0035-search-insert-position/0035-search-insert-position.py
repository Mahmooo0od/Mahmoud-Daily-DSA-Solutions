class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        i=0 
        J=len(nums)-1 
        mid=(J+i)//2 
        if target >nums[J] : 
            return J+1
        elif target<nums[i] : 
            return i 

        while i<=J : 
            if target>nums[mid] : 
                i=mid+1 
                mid=(J+i)//2 
            elif target<nums[mid] :
                J=mid-1
                mid=(J+i)//2 
            else : 
                return mid 
        return i
                
        