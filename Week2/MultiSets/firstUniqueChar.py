from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        res = [s.find(x) for x in counter if counter[x] == 1]
        if not res:
            return -1
        return res[0]