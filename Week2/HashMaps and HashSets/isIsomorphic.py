class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Below passes 29/30 test cases: O(n) runtime
        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        maskS = [s[i] == s[i+1] for i in range(len(s)-1)]
        maskT = [t[i] == t[i+1] for i in range(len(t)-1)]
        if maskS != maskT:
            return False
        return True
    