# https://leetcode.com/problems/ransom-note/
# https://leetcode.com/problems/ransom-note/submissions/1032570646/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        mag = Counter(magazine)
        for key in note:
            if key not in mag or note[key] > mag[key]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.canConstruct('a', 'b') is False
    assert sol.canConstruct('aa', 'aba') is True
    # assert sol.canConstruct('aca', 'aaabbb') is True
