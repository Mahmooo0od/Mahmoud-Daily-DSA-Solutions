class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        f1=str1+str2 
        f2=str2+str1
        if f1 == f2 : 
            return str1[:math.gcd(len(str1),len(str2))]
        else : 
            return "" 

        