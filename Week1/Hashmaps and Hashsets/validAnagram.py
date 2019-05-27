class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        for x in set(s):
            if s.count(x) != t.count(x):
                return False
        return True
            