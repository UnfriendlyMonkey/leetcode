# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1314964981/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        all_letters = {}
        singles = {}
        for idx, letter in enumerate(s):
            if letter not in all_letters:
                all_letters[letter] = True
                singles[letter] = idx
            else:
                all_letters[letter] = False
                if letter in singles:
                    singles.pop(letter)
        if not singles:
            return -1
        return sorted(singles.values())[0]


class Solution_fastest:
    def firstUniqChar(self, s: str) -> int:
        s1 = s
        while len(s) > 0:
            a = s[0]
            s = s.replace(a, "", 1)
            if a in s:
                s = s.replace(a, "")
            else:
                return s1.find(a)
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.firstUniqChar("aabb") == -1
    assert s.firstUniqChar("leetcode") == 0
    assert s.firstUniqChar("loveleetcode") == 2
