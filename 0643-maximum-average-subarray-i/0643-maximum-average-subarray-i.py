class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        i=0 
        n=len(nums) 
        sums = sum(nums[:k])*1.00000 
        J=k
        maxx=sums 
        while J<n : 
            sums=(sums-nums[i])+nums[J]
            maxx=max(sums,maxx)
            J+=1
            i+=1
        return maxx/k
