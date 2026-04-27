class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,x in enumerate(citations):
            if n - i <= x:
                return n - i
        return 0