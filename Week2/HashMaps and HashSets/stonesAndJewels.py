class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0
        count = 0
        for x in J:
            count += S.count(x)
        return count