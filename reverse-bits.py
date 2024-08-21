# https://leetcode.com/problems/reverse-bits/submissions/973319111/

class Solution:
    def reverseBits(self, n: int) -> int:
        # converted = bin(n)[2:].zfill(32)
        converted = bin(n)[2:].rjust(32, '0')
        reversed = converted[::-1]
        return int(reversed, 2)


sol = Solution()
assert sol.reverseBits(43261596) == 964176192
assert sol.reverseBits(4294967293) == 3221225471
