# https://leetcode.com/problems/longest-palindrome/description/
# https://leetcode.com/problems/longest-palindrome/submissions/1332015412/
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        sum = 0
        has_odd = False
        for i in counter.values():
            if not i % 2:
                sum += i
            elif not has_odd:
                sum += i
                has_odd = True
            else:
                sum += i - 1
        return sum


sol = Solution()
s = "abccccdd"
print(sol.longestPalindrome(s))
s = "a"
print(sol.longestPalindrome(s))
