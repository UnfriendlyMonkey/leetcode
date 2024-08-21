# https://leetcode.com/problems/valid-palindrome/submissions/956573765/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [l.lower() for l in s if l.isalnum()]
        pure_str = ''.join(string)
        index = len(pure_str) // 2
        if not len(pure_str) % 2:
            return pure_str[:index] == ''.join(reversed(pure_str[index:]))
        else:
            return pure_str[:index] == ''.join(reversed(pure_str[index + 1:]))


st = 'A man, a plan, a canal: Panama'
st = 'race a car'
sol = Solution()
print(sol.isPalindrome(st))
