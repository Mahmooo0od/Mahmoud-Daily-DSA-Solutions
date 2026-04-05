class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         k = 0 
         i=0
         J=0 
         while J<len(nums): 
            if nums[J]!=val : 
                nums[J],nums[i]=nums[i],nums[J] 
                i+=1
                k+=1
            J+=1 
         return k