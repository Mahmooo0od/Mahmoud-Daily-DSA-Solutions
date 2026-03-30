class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        i=0 
        n=len(nums) 
        sums = sum(nums[:k])*1.00000 
        J=k
        Avg=(sums/k)
        maxx=Avg 
        while J<n : 
            sums=(sums-nums[i])+nums[J]
            Avg=(sums/k)
            maxx=max(Avg,maxx)
            J+=1
            i+=1
        return maxx
