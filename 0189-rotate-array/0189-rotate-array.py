class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N=len(nums)
        r=k % N  
        def reversee(L,R) : 
            while L<R :
                nums[L],nums[R]=nums[R],nums[L] 
                R-=1 
                L+=1 
        reversee(0,N-1) 
        reversee(0,r-1) 
        reversee(r,N-1) 
        return nums