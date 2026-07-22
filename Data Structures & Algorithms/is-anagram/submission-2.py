class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_s = {}
        word_t = {}
        for i in range(len(s)):
            word_s[s[i]] = word_s.get(s[i],0) + 1
            word_t[t[i]] = word_t.get(t[i],0) + 1
        if word_s != word_t:
            return False
        return True
