from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s).most_common() 
        return ''.join([x[0] * x[1] for x in counter])
        