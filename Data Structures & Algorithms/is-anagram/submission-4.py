class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charsS, charsT = {}, {}
        for i in range(len(s)):
            charsS[s[i]] = 1 + charsS.get(s[i], 0)
            charsT[t[i]] = 1 + charsT.get(t[i], 0)
        return charsS == charsT