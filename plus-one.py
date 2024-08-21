# https://leetcode.com/problems/plus-one/submissions/876755446/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st_digits = ''.join(str(i) for i in digits)
        st_plus_one = str(int(st_digits) + 1)
        plus_one = [int(i) for i in st_plus_one]
        return plus_one


digits = [1, 2, 3]
s = Solution()
print(s.plusOne(digits))

digits = [1, 3, 9, 9]
print(s.plusOne(digits))
