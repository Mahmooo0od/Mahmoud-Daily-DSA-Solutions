class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s) 
        indicator=0 
        c=0 
        J=0
        for i in range(n-1,-1,-1) : 
            J+=1
            if s[i]!=' ' :
                indicator=1 
                c+=1

            if s[i]==' ' and indicator==1 :
                return c
        return c