# https://leetcode.com/problems/pascals-triangle/submissions/963616336/


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * row for row in range(1, numRows + 1)]

        if numRows > 2:
            for row in range(2, numRows):
                for cell in range(1, row):
                    result[row][cell] = (
                        result[row - 1][cell - 1] + result[row - 1][cell]
                    )
        return result


sol = Solution()
# print(sol.generate(1))
# print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(4))
print(sol.generate(7))
