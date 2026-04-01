class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Dict=Counter(arr)

        return len(Dict.values())==len(set(Dict.values()))