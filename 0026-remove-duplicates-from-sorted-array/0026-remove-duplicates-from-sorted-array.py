class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        set1=set(nums) 
        K=len(set1) 
        nums.sort()
        i=0
        while i<K : 
            if nums[i]==nums[i-1] and i!=0:
                nums.append(nums[i])
                nums.pop(i) 
            else : 
                i+=1 
        return K

        