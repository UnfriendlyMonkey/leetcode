# https://leetcode.com/problems/reverse-string/submissions/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


sol = Solution()
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
assert s == ["o", "l", "l", "e", "h"]
s = ["H", "a", "p", "n", "a", "h"]
sol.reverseString(s)
assert s == ["h", "a", "n", "p", "a", "H"]
s = ['a', 'a']
sol.reverseString(s)
assert s == ['a', 'a']
s = ['b', 'a']
sol.reverseString(s)
assert s == ['a', 'b']
s = ['a']
sol.reverseString(s)
assert s == ['a']
