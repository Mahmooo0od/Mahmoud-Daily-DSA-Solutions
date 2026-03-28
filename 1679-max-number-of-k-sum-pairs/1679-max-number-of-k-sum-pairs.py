class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        Dict={}
        c=0
        for i in range(len(nums)): 
            oppo=k-nums[i]
            if Dict.get(oppo,0) >0 : 
                Dict[oppo]-=1 
                c+=1
            else : 
                Dict[nums[i]]=Dict.get(nums[i],0)+1
        return c
            
        return c