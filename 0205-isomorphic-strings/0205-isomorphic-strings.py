class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 
        if len(s)!=len(t): 
            return False

        dict={} 

        for i,j in zip(s,t):
            if dict.get(i,0) : 
                if dict[i]==j: 
                    pass 
                else: 
                    return False 
            else : 
                dict[i]=j

            
        return len(dict.values())==len(set(dict.values()))
                