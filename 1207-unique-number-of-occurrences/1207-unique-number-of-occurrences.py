class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Dict={}
        for i in arr : 
            Dict[i]=Dict.get(i,0)+1
        set1=set(Dict.values())
        return len(Dict.values())==len(set1)