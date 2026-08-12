class Solution:
    def isHappy(self, n: int) -> bool:
        set_1=set()
        c=0 
        New=0 

        while 1==1 : 
            if c>len(set_1): 
                return False 
            while n>0 : 
                L=n%10 
                n//=10 
                New=New+pow(L,2) 
            if New==1: 
                return True 
            else : 
                n=New 
                set_1.add(New)
                c+=1
                New=0
        