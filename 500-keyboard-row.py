# https://leetcode.com/problems/keyboard-row/description
# https://leetcode.com/problems/keyboard-row/submissions/1380378390


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # rather fast but memory-inefficient
        rows = [set('qwertyuiop'), set("asdfghjkl"), set('zxcvbnm')]
        return [
            w for w in words if any(set(w.lower()).issubset(r) for r in rows)
        ]


def main():
    sol = Solution()
    words = ["Hello","Alaska","Dad","Peace"]
    print(sol.findWords(words))
    words = ["omk"]
    print(sol.findWords(words))
    words = ["adsdf","sfd"]
    print(sol.findWords(words))


if __name__ == '__main__':
    main()
