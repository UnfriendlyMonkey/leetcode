# https://leetcode.com/problems/is-subsequence/description/
# https://leetcode.com/problems/is-subsequence/submissions/1324178248/
#
#
class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        idx = 0
        for letter in s:
            try:
                idx = t.index(letter, idx) + 1
                print(f"{letter=}, {idx=}")
            except ValueError as err:
                print(f"error: {letter=}, {idx=}")
                return False
        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        # faster and not mine
        # idea is to move along longer string and move search index of short in case of match
        s_idx = 0
        for char in t:
            if s_idx == len(s):
                break
            if s[s_idx] == char:
                s_idx += 1
        return s_idx == len(s)


if __name__ == "__main__":
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc") is True
    assert s.isSubsequence("axc", "ahbgdc") is False
    assert s.isSubsequence("aaaaaa", "bbaaaa") is False
