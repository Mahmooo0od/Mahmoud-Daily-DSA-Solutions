class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        freq_1={}
        freq_2={}
        for i in s :
            freq_1[i]=freq_1.get(i,0)+1 

        for i in t :
            freq_2[i]=freq_2.get(i,0)+1 
        
        return freq_1==freq_2
        

        