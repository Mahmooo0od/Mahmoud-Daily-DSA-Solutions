class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for f,j in enumerate(nums):
            if target-j in dict :
                res=[dict[target-j],f]
                return res 
            else : 
                dict[j]=f