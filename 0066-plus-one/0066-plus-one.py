class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1] += 1 
            return digits 
        else: 
            i = len(digits) - 1
            k = 0
            while i >= 0 and digits[i] == 9: 
                digits[i] = 0 
                k += 1
                i -= 1
            
            if i == -1:  
                return [1] + digits 
        
            else:
                digits[i] += 1
                return digits