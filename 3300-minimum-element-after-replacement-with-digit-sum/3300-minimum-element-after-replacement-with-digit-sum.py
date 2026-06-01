class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            To = 0

            while num > 0:
                To += (num % 10)
                num //= 10

            ans = min(ans, To)

        return ans