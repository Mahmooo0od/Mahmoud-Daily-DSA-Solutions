class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        set1=set(nums) 
        K=len(set1) 
        nums.sort()
        i=0
        while i<K : 
            if i==0 : 
                i+=1
                continue
            if nums[i]==nums[i-1]:
                nums.append(nums[i])
                nums.pop(i) 
            else : 
                i+=1 
        return K

        