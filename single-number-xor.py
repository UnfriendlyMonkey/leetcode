# https://leetcode.com/problems/single-number/submissions/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for number in nums:
            # twice xor the same number gives us 0
            # so we left with unique one at the end
            xor ^= number
        return xor
