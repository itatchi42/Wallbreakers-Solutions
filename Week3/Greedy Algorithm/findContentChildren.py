class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Base case
        if not g or not s:
            return 0
        
        # More efficient way (sort first, THEN search in linear time)
        # Runtime: O(logn)
        g.sort()
        s.sort()
        
        greed, size, numHappy = 0, 0, 0
        while greed < len(g) and size < len(s):
            if s[size] >= g[greed]:
                numHappy += 1
                greed += 1 # Next kid
            size += 1 # Next cookie
        return numHappy
        
        # Naive way: O(n^2) where I iterate over s for each ele in g
        # Runtime: O(n^2)
        # numCookies, numHappy = len(s), 0
        # for greed in g:
        #     for size in s:
        #         if size >= greed:
        #             numHappy = min(numCookies, numHappy + 1)
        #             break # See if I can make next child happy
        # return numHappy
        
        
                    
        
