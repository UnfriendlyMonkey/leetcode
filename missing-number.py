# https://leetcode.com/problems/missing-number/submissions/988157681/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = sum(range(len(nums) + 1))
        return s2 - s1

    def missingNumber2(self, nums: List[int]) -> int:
        # gauss formula
        # time: O(n), space O(1)
        n = len(nums) + 1
        s1 = sum(nums)
        s2 = n * (n - 1) // 2
        return s2 - s1

    def missingNumberXor(self, nums: List[int]) -> int:
        # the trick is the same as in finding the only non-duplicate by xor
        # we are adding each value twice by (1) adding itself and
        # (2) adding its index (including the last one in first line)
        # the only value included once is the missing value
        # so it will be left alone after all xor operations done
        result = len(nums)
        for i, v in enumerate(nums):
            result ^= i ^ v
        return result


sol = Solution()
arr = [3, 0, 1]
print(sol.missingNumber(arr) == sol.missingNumber2(arr))
