# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x: x[::-1], s.split()))
