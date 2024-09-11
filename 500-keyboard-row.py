# https://leetcode.com/problems/keyboard-row/description
# https://leetcode.com/problems/keyboard-row/submissions/1380378390


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # rather fast but memory-inefficient
        rows = [set('qwertyuiop'), set("asdfghjkl"), set('zxcvbnm')]
        return [
            w for w in words if any(set(w.lower()).issubset(r) for r in rows)
        ]

    def findWords2(self, words: list[str]) -> list[str]:
        # others solution not obvious but interesting
        # better in memory, slower in speed
        rows = [set('qwertyuiop'), set("asdfghjkl"), set('zxcvbnm')]
        res = []
        for word in words:
            current = set()

            for r in rows:
                if word[0].lower() in r:
                    current = r
                    break

            for letter in word[1:]:
                if letter.lower() not in current:
                    break
            else:
                res.append(word)

        return res



def main():
    sol = Solution()
    words = ["Hello","Alaska","Dad","Peace"]
    print(sol.findWords(words))
    print(sol.findWords2(words))
    words = ["omk"]
    print(sol.findWords(words))
    print(sol.findWords2(words))
    words = ["adsdf","sfd"]
    print(sol.findWords(words))
    print(sol.findWords2(words))


if __name__ == '__main__':
    main()
