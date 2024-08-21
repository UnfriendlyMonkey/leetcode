# https://leetcode.com/problems/valid-anagram/submissions/987042289/
from collections import Counter
from itertools import zip_longest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)
        return all(
            [a == b for a, b in zip_longest(
                sorted(cs.items()), sorted(ct.items())
            )]
        )

    def isAnagram2(self, s, t):
        cs = Counter(s)
        ct = Counter(t)
        return cs == ct


sol = Solution()
assert sol.isAnagram('anagram', 'nagaram') is True
assert sol.isAnagram('rat', 'tag') is False
assert sol.isAnagram('ab', 'a') is False
