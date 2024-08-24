# https://leetcode.com/problems/repeated-substring-pattern/
# https://leetcode.com/problems/repeated-substring-pattern/submissions/1367087693/
import math


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        middle = math.ceil(len(s) / 2) + 1
        for idx in range(1, middle):
            base, remain = divmod(len(s), idx)
            print(f'{idx=}, {base=}, {remain=}')
            if remain:
                continue
            substring = s[:idx]
            print(f'{substring=}, {base=}, {remain=}')
            if substring * base == s:
                return True

        return False


def main():
    sol = Solution()
    s = "abab"
    assert sol.repeatedSubstringPattern(s) is True
    s = "aba"
    assert sol.repeatedSubstringPattern(s) is False
    s = "abcabcabcabc"
    assert sol.repeatedSubstringPattern(s) is True


if __name__ == "__main__":
    main()
