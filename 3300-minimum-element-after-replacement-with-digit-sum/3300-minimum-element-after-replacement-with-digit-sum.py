class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            T = 0

            while num > 0:
                T += (num % 10)
                num //= 10

            ans = min(ans, T)

        return ans