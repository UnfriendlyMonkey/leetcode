# https://leetcode.com/problems/find-the-difference/
# https://leetcode.com/problems/find-the-difference/submissions/1323222786/
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        cs = Counter(s)
        ct = Counter(t)
        res = next((ct - cs).elements())
        # print(res)
        return res

    def findTheDifference2(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) > s.count(i):
                return i


if __name__ == "__main__":
    sol = Solution()
    assert sol.findTheDifference("abcd", "abcde") == "e"
    assert sol.findTheDifference("", "y") == "y"
    assert sol.findTheDifference2("abcd", "abcde") == "e"
    assert sol.findTheDifference2("", "y") == "y"
