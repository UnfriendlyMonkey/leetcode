# https://leetcode.com/problems/detect-capital
# string
# https://leetcode.com/problems/detect-capital/submissions/1387007421
# beats 81.67 in time and 39.13 in memory


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        if word.capitalize() == word:
            return True
        if word[:2].lower() == word[:2]:
            return word.lower() == word
        if word[:2].upper() == word[:2]:
            return word.upper() == word
        return False


def main():
    sol = Solution()
    word = 'I'
    print(sol.detectCapitalUse(word))
    word = 'USA'
    print(sol.detectCapitalUse(word))
    word = 'leetcode'
    print(sol.detectCapitalUse(word))
    word = 'FlaG'
    print(sol.detectCapitalUse(word))
    word = 'FFFFFFFFFFFFFFFFFFFFf'
    print(sol.detectCapitalUse(word))
    word = 'Leetcode'
    print(sol.detectCapitalUse(word))


main()
