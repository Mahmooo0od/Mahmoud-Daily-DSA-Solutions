class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==0 or len(height)==1 : 
            return 0

        maxx = float('-inf') 
        Sakln=True 
        i=0 
        J=len(height)-1 
        while i<J : 
            minn=min(height[i],height[J])
            Area=(J-i)*minn
            maxx=max(Area,maxx) 
            if height[i]>=height[J] : 
                J-=1 
            else : 
                i+=1 
        return maxx