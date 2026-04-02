class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2) : 
            return False 
        Dict1={} 
        Dict2={}

        for i in range(len(word1)) : 
            Dict1[word1[i]]=Dict1.get(word1[i],0)+1
            Dict2[word2[i]]=Dict2.get(word2[i],0)+1 
        if Dict1==Dict2 : 
            return True 
        else : 
            DL1=list(Dict1.values())
            DL2=list(Dict2.values())
            DL1.sort() 
            DL2.sort() 
            B=DL1==DL2
            for i in Dict1.keys() : 
                for J in Dict2.keys(): 
                    if Dict1[i]==Dict2[J] and i!=J and Dict1.keys()==Dict2.keys() and B: 
                        return True 
            return False 
                    


        