# https://leetcode.com/problems/valid-parentheses/submissions/862315302/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = '({[)}]'
        check_str = ''
        for item in s:
            if item in brackets[:3]:
                check_str += item
            elif len(check_str) == 0:
                return False
            elif check_str.endswith(brackets[brackets.index(item) - 3]):
                check_str = check_str[:-1]
            else:
                return False
        return True if check_str == '' else False


result = Solution()
print(result.isValid('(]{}'))

