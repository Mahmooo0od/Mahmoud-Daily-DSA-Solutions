class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx=0
        for i in range(len(gain)): 
            if i==0 :
                pass
            else:
                gain[i]=gain[i]+gain[i-1] 
            if gain[i]>maxx :
                maxx=gain[i] 
        return maxx 
        