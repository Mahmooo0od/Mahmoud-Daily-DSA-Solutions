class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        strs.sort() 
        L=strs[0] 
        R=strs[-1] 
        ansss=""
        for i in range(min(len(L),len(R))) :
            if L[i]==R[i] : 
                ansss+=L[i] 
            else : 
                break 
        return ansss
        