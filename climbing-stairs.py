# https://leetcode.com/problems/climbing-stairs/
# didn't pass - exceeded time limit


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


sol = Solution()
n = 3
print(sol.climbStairs(n))
