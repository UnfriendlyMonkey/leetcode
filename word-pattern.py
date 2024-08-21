# https://leetcode.com/problems/word-pattern/submissions/994624051/
# not efficient
# https://leetcode.com/problems/word-pattern/submissions/994630300/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split()
        if len(pattern) != len(split_s):
            return False
        if len(set(pattern)) != len(set(split_s)):
            return False
        num_pattern = [pattern.index(i) for i in pattern]
        s_pattern = [split_s.index(j) for j in split_s]
        return num_pattern == s_pattern

    def wordPattern2(self, pattern: str, s: str) -> bool:
        # dictionary approach
        # Time complexity: O(n)
        # Space complexity: O(n)

        words = s.split(" ")
        if not len(words) == len(pattern):
            return False

        mapping = dict()  # key is the pattern, value is the word

        for i in range(len(words)):
            if pattern[i] not in mapping:
                # values() is a set - fast membership testing
                # - O(1) amortised search
                if words[i] not in mapping.values():
                    mapping[pattern[i]] = words[i]
                else:
                    return False
            else:
                if not mapping[pattern[i]] == words[i]:
                    return False
        return True


sol = Solution()
s = 'dog cat cat dog'
s2 = 'dog cat cat fish'
print(sol.wordPattern('abba', s))
print(sol.wordPattern('abba', s2))
print(sol.wordPattern('aaaa', s))
