# https://leetcode.com/problems/excel-sheet-column-title/submissions/968060047/

from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cur = columnNumber
        result = ''
        while cur > 26:
            result += ascii_uppercase[cur % 26 - 1]
            cur = (cur - 1) // 26
        result += ascii_uppercase[cur - 1]
        return result[::-1]

    def convertToTitle2(self, columnNumber: int) -> str:
        # faster
        result = ''
        while columnNumber:
            columnNumber -= 1
            result = ascii_uppercase[columnNumber % 26] + result
            columnNumber //= 26
        return result


sol = Solution()

print(sol.convertToTitle(1))
print(sol.convertToTitle(26))
print(sol.convertToTitle(27))
print(sol.convertToTitle(51))
print(sol.convertToTitle(52))
print(sol.convertToTitle(701))
print(sol.convertToTitle(703))
print(sol.convertToTitle(256874))
