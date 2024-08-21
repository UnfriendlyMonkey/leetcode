# https://leetcode.com/problems/power-of-four/submissions/1000175044/
# https://leetcode.com/problems/power-of-four/submissions/1000180330/
from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        pow = round(log(n, 4))
        return 4 ** pow == n

    def isPowerOfFour2(self, n: int) -> bool:
        if n < 1:
            return False
        while n & 3 == 0:
            n = n >> 2
        return n == 1


sol = Solution()
assert sol.isPowerOfFour(16) is True
assert sol.isPowerOfFour(5) is False
assert sol.isPowerOfFour(1) is True
assert sol.isPowerOfFour(-16) is False
