# https://leetcode.com/problems/pascals-triangle/submissions/963627432/
# https://leetcode.com/problems/pascals-triangle/submissions/963631046/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for row in range(1, numRows):
            list1 = result[-1] + [0]
            list2 = [0] + result[-1]
            cells = [list1[x] + list2[x] for x in range(row + 1)]
            result.append(cells)
            # slower but more memory efficient
            # result += [list(map(
            #     lambda x, y: x + y, [0] + result[-1], result[-1] + [0]
            # ))]
        return result


sol = Solution()
# print(sol.generate(1))
print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(4))
print(sol.generate(7))
