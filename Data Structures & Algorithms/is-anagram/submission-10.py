class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = {}
        d = {}
        for i in range(len(s)):
            a[s[i]] = 1 + a.get(s[i], 0 )
            d[t[i]] = 1 + d.get(t[i], 0 )
        
        return a == d
        