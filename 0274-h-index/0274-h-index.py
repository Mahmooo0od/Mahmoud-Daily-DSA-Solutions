class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()

        for i,x in enumerate(citations):
            if N - i <= x:
                return N - i
        return 0