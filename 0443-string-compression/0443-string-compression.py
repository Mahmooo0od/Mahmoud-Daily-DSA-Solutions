class Solution:
    def compress(self, chars: List[str]) -> int:
        c=1
        res=[]
        n=len(chars)
        for i in range(n) : 
            if i+1<n and chars[i]==chars[i+1] : 
                c+=1 
            else : 
                res.append(chars[i])
                if c>1 : 
                    res.extend(str(c))
                c=1 
        n_res=len(res)
        chars[:n_res]=res
        return n_res
