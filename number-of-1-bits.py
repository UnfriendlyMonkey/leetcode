# https://leetcode.com/problems/number-of-1-bits/submissions/973451613/


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


sol = Solution()
assert sol.hammingWeight(11) == 3
