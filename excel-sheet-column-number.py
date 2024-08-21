# https://leetcode.com/problems/excel-sheet-column-number/submissions/969570719/
# beats 78 in speed, 72 in memory
# https://leetcode.com/problems/excel-sheet-column-number/submissions/969577164/
# this one is worse both in speed and memory

from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pow = len(columnTitle) - 1
        result = 0
        for letter in columnTitle:
            value = 26 ** pow * (ascii_uppercase.index(letter) + 1)
            pow -= 1
            result += value
        return result

    def titleToNumber2(self, columnTitle: str) -> int:
        result = 0
        for pow, letter in enumerate(columnTitle[::-1]):
            value = 26 ** pow * (ascii_uppercase.index(letter) + 1)
            result += value
        return result


sol = Solution()
print(sol.titleToNumber('A'))
print(sol.titleToNumber('AB'))
print(sol.titleToNumber('ZY'))
print(sol.titleToNumber('AAA'))
print(sol.titleToNumber('NOYT'))
