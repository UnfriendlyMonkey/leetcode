# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
from timeit import timeit


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        if n_len == 0:
            return 0
        h_len = len(haystack)

        for i in range(h_len - n_len + 1):
            found = True
            for j in range(n_len):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            if found is True:
                return i
        return -1


sol = Solution()
hay = 'badbutsad'
nee = 'sad'
print(sol.strStr(hay, nee))
print(timeit('Solution().strStr(hay, nee)', globals=globals(), number=10000))
print(timeit('hay.find(nee)', number=10000, globals=globals()))
