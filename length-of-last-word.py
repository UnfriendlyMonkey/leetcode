# https://leetcode.com/problems/length-of-last-word/submissions/875649753/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit()[-1])
