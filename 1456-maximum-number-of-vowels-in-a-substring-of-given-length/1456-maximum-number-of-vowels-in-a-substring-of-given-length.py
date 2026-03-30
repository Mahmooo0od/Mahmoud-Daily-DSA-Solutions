class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v_set={'a','e','o','u','i'}   
        sums=0 

        for J in range(k): 
            if s[J] in v_set : 
                sums+=1 
        J=k
        maxx=sums 
        i=0 
        for J in range(J,len(s)) :
            if s[J] in v_set and s[i] not in v_set : 
                sums+=1 
                if sums>maxx : 
                    maxx=sums 
            elif s[J] not in v_set and s[i] in v_set :
                sums-=1 
            i+=1 
        return maxx
            

        