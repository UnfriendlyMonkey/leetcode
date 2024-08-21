# https://leetcode.com/problems/climbing-stairs/
# didn't pass - exceeded time limit


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


sol = Solution()
n = 7
print(sol.climbStairs(n))
