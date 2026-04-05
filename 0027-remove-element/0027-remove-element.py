class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         k = 0 
         J=0 
         while J<len(nums): 
            if nums[J]!=val : 
                nums[J],nums[k]=nums[k],nums[J] 
                k+=1
            J+=1 
         return k