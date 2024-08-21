# https://leetcode.com/problems/isomorphic-strings/979315830/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in range(len(s)):
            sd.setdefault(s[i], []).append(i)
            td.setdefault(t[i], []).append(i)
        return sorted(sd.values()) == sorted(td.values())

    def isIsomorphic2(s, t):
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

    def isIsomorphic3(s, t):
        # maps each letter to index of its first position
        return [*map(s.index, s)] == [*map(t.index, t)]


sol = Solution()
s = 'egg'
t = 'add'
assert sol.isIsomorphic(s, t) is True
s = 'foo'
t = 'bar'
assert sol.isIsomorphic(s, t) is False
s = 'bbbaaaba'
t = 'aaabbbba'
assert sol.isIsomorphic(s, t) is False
s = 'paper'
t = 'title'
assert sol.isIsomorphic(s, t) is True
