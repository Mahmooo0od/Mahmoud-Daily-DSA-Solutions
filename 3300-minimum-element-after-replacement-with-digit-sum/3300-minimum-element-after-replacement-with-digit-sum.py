class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            Too = 0

            while num > 0:
                Too += (num % 10)
                num //= 10

            ans = min(ans, Too)

        return ans