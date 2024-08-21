# https://leetcode.com/problems/single-number/submissions/965735766/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for number in nums:
            is_second = num_dict.get(number, 0)
            if not is_second:
                num_dict[number] = 1
            else:
                num_dict.pop(number)
        return list(num_dict)[0]
