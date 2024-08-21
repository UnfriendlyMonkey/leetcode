# https://leetcode.com/problems/pascals-triangle-ii/submissions/964239093/

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)

        for row in range(2, rowIndex + 1):
            previous = 1
            for cell in range(1, row):
                reserve = result[cell]
                result[cell] = (
                    previous + reserve
                )
                previous = reserve
        return result


sol = Solution()
print(sol.getRow(0))
print(sol.getRow(1))
print(sol.getRow(2))
print(sol.getRow(3))
print(sol.getRow(4))
print(sol.getRow(7))
