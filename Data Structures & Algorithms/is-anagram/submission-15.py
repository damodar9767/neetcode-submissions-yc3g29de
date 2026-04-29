class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        for c in s:
            if c in a:
                a[c] = a.get(c,0) + 1
            else:
                a[c] = 1
        
        for c in t:
            if c in b:
                b[c] = b.get(c,0) + 1
            else:
                b[c] = 1
        
        return a == b 