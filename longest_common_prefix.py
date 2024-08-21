# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        result = ''
        for letter in range(len(strs[0])):
            current = strs[0][letter]
            if not all([len(word) > letter
                        and word[letter] == current for word in strs]):
                break
            result += current
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ''
    assert solution.longestCommonPrefix([""]) == ''
    assert solution.longestCommonPrefix(["ab", "a"]) == 'a'
