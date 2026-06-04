class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            Tooo = 0

            while num > 0:
                Tooo += (num % 10)
                num //= 10

            ans = min(ans, Tooo)

        return ans