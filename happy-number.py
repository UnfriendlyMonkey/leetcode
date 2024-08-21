# https://leetcode.com/problems/happy-number/submissions/977735036/


class Solution:
    def isHappy(self, n: int) -> bool:
        passed = set()
        while True:
            if n == 1:
                return True
            if n == 2:
                return False
            digits = [int(d) ** 2 for d in str(n)]
            n = sum(digits)
            if n in passed:
                return False
            passed.add(n)


sol = Solution()
assert sol.isHappy(2) is False
assert sol.isHappy(19) is True
assert sol.isHappy(3) is False
