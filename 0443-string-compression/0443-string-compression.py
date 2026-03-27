class Solution:
    def compress(self, chars: List[str]) -> int:
        left=0 
        right=0
        while left<len(chars) :
            current=chars[left]
            c=0
            while left<len(chars) and current==chars[left] :
                left+=1
                c+=1
            ## left !=current 
            chars[right]=current 
            right+=1 
            if c>1 : 
                for i in str(c) :
                    chars[right]=i 
                    right+=1 
        return right