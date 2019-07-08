from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #Runtime: O(n^2) b/c the string.split()
        counter = Counter()
        for url in cpdomains:
            #Seperate the num from the rest of string
            string = url.split(' ')
            num, remain = string[0], string[1]
            counter.update({remain : int(num)}) #Adding full RL
            theSplit = remain.split('.')
            lenSplit = len(theSplit)
            #Add mid + top level domains
            if lenSplit == 3: counter.update({'.'.join(theSplit[1 : ]) : int(num)})
            #Add just top level domain
            counter.update({theSplit[-1] : int(num)}) #add just first part
        res = []
        for val in counter:
            res.append(str(counter[val]) + ' ' + val)
        return res
        