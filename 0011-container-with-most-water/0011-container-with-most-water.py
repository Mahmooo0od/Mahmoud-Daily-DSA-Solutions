class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==0 or len(height)==1 : 
            return 0

        maxx = -1 
        i=0 
        J=len(height)-1 
        while i<J : 
            minn=min(height[i],height[J])
            Area=(J-i)*minn
            maxx=max(Area,maxx) 
            if height[i]>=height[J] : 
                J-=1 
            elif height[i]<height[J]: 
                i+=1 
            else : 
                i+=1 
                J-=1
        return maxx