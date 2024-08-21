# https://leetcode.com/problems/counting-bits/submissions/991165952/
# https://leetcode.com/problems/counting-bits/submissions/991178640/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # slower but better in memory
        return [bin(d).count('1') for d in range(n + 1)]

    def countBits2(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            if n % 2:
                result[i] = result[i - 1] + 1
            else:
                result[i] = result[i // 2]
        return result

    def countBits3(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i // 2] + i % 2)  # the same as previous
            # - odds have one more 'ones' than previous even
        return res


sol = Solution()
assert sol.countBits(2) == [0, 1, 1]
assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
