class Solution:
    def isHappy(self, n: int) -> bool:
        set_1=set() 
        New=0 

        while True :  
            while n>0 : 
                L=n%10 
                n//=10 
                New=New+L**2 
            if New==1: 
                return True 
            else : 
                n=New 
                if New in set_1: 
                    return False
                set_1.add(New)
                New=0
        