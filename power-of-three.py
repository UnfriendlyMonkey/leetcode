# https://leetcode.com/problems/power-of-three/submissions/999444378/


from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while not n % 3:
            n //= 3
        return n == 1

    def isPowerOfThree2(self, n: int) -> bool:
        if n < 1:
            return False
        pow = round(log(n, 3))
        # find max pow available <= n
        return 3 ** pow == n


sol = Solution()
assert sol.isPowerOfThree(27) is True
assert sol.isPowerOfThree(0) is False
assert sol.isPowerOfThree(-1) is False
