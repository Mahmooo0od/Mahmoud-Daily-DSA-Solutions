class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for o,j in enumerate(nums):
            if target-j in dict :
                res=[dict[target-j],o]
                return res 
            else : 
                dict[j]=o