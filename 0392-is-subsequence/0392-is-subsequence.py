class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        read=0 
        if len(s)==0 :
            return True 
        for i in range(len(t)) : 
            if t[i]==s[read] :
                read+=1 
                if read==len(s):
                    return True 
        return False

