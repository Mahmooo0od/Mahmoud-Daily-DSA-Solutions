class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 1  
        result = 0
        
        for bed in flowerbed:
            if bed == 0:
                count += 1
            else:
                result += (count - 1) // 2
                count = 0 
                
        count += 1
        result += (count - 1) // 2
        
        return result >= n