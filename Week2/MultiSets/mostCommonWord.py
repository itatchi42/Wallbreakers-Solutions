from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #Strip paragraph of punctuation, make it lowercase, and conv to list
        stripped = re.split('\W+', paragraph.lower()) #'\W+' = Find 1+ occurences of non-words
        #Add each word to counter
        counter = Counter(x for x in stripped if x and x not in banned)
        #Return most common word from counter
        return counter.most_common(1)[0][0]
