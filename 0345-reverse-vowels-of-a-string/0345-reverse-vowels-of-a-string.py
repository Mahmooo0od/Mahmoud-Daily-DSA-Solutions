class Solution:
    def reverseVowels(self, s: str) -> str:
        p1=0 
        p2=len(s)-1 
        res=list(s) 
        vowels = set("aeiouAEIOU")
        while p1<=p2 :
            if res[p1] in vowels :
                flag1=1 
            else : 
                flag1=0 

            
            if res[p2] in vowels :
                flag2=1 
            else :
                flag2=0 


            if flag1==1 and flag2==1 :
                swap=res[p1] 
                res[p1]=res[p2]
                res[p2]=swap 
                p1+=1 
                p2-=1
            elif flag1==1 and flag2==0 : 
                p2-=1 
            elif flag1==0 and flag2==1 : 
                p1+=1 
            else : 
                p1+=1 
                p2-=1 
        s="".join(res)
        return s