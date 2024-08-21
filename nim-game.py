# https://leetcode.com/problems/nim-game/submissions/994998555/

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


sol = Solution()
assert sol.canWinNim(4) is False
assert sol.canWinNim(3) is True
assert sol.canWinNim(1) is True
assert sol.canWinNim(16) is False
