class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        c = 0
        for x in gain : 
            c+=x 
            if c > maxx : 
                maxx=c 
        return maxx
        
        
        