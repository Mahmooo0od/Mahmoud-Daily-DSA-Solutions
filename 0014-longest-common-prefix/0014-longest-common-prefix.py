class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        strs.sort() 
        L=strs[0] 
        R=strs[-1] 
        anss=""
        for i in range(min(len(L),len(R))) :
            if L[i]==R[i] : 
                anss+=L[i] 
            else : 
                break 
        return anss
        