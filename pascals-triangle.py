# https://leetcode.com/problems/pascals-triangle/submissions/963608450/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows > 0:
            result.append([1])
        if numRows > 1:
            result.append([1, 1])
        if numRows > 2:
            for row in range(3, numRows + 1):
                cells = [1]
                prev_row = result[-1]
                for cell in range(1, row - 1):
                    cells.append(prev_row[cell - 1] + prev_row[cell])
                cells.append(1)
                result.append(cells)
        return result


sol = Solution()
# print(sol.generate(1))
# print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(4))
print(sol.generate(7))
