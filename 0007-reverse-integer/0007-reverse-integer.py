class Solution:
    def reverse(self, x: int) -> int:
        X = str(x)
        X_list = list(X)
        
        if X_list[0] == '-' :
            i = 1
        else : 
            i=0 
        
        J = 0
        
        while J < (len(X_list) - i) // 2:
            X_list[i + J], X_list[len(X_list) - 1 - J] = X_list[len(X_list) - 1 - J], X_list[i + J]
            J += 1
        
        X = "".join(X_list)
        Final = int(X)
        
        if Final < -2**31 or Final > 2**31 - 1:
            return 0
            
        return Final