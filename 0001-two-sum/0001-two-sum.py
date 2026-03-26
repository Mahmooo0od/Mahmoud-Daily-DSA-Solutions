class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,j in enumerate(nums):
            if target-j in dict :
                res=[dict[target-j],i]
                return res 
            else : 
                dict[j]=i
