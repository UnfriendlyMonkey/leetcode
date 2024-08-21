# https://leetcode.com/problems/reverse-vowels-of-a-string/
# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1001309018/
# beats 96% in speed but only 16% in memory
# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1001313190/
# beats 61% in speed and 84% in memory


class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = 'aeiou'
        split_s = list(s)
        vow_idxs = [i for i, l in enumerate(split_s) if l.lower() in vows]
        if len(vow_idxs) > 1:
            for j in range(len(vow_idxs) // 2):
                (split_s[vow_idxs[j]], split_s[vow_idxs[~j]]) = (
                        split_s[vow_idxs[~j]], split_s[vow_idxs[j]])
        return ''.join(split_s)

    def reverseVowels2(self, s: str) -> str:
        vows = 'aeiou'
        split_s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if split_s[i].lower() not in vows:
                i += 1
            elif split_s[j].lower() not in vows:
                j -= 1
            else:
                split_s[i], split_s[j] = split_s[j], split_s[i]
                i += 1
                j -= 1
        return ''.join(split_s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels2('hello'))
    print(sol.reverseVowels2('leetcode'))
    print(sol.reverseVowels2(
        'In written English the six vowel letters are used to represent the'))
