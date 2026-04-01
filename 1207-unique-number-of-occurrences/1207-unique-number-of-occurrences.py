class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Dict={}
        for i in arr : 
            Dict[i]=Dict.get(i,0)+1
            
        return len(Dict.values())==len(set(Dict.values()))