class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #check if both lists empty
        if not g or not s:
            return 0
       
        g.sort()
        s.sort() #to make sure I'm getting correct NEXT greatest num
        
        count = 0
        indx = -1
        #default -1 if didn't find cookie >= curr child's greed factor
        for factor in g:
            indx = next((x[0] for x in enumerate(s) if x[1] >= factor), -1) #Do I have cookie >= greed?
            if indx >= 0: 
                s.pop(indx) #Cannot reassign cookies
                count += 1
        return count 

 
#         g.sort()
#         s.sort()
        
#         i, j, count = 0, 0, 0
#         while j < len(g) and i < len(s):
#             print(i)
#             print(j)
#             if s[i] >= g[j]: #I have cookie >= greed?
#                 print('yup')
#                 count += 1
#                 j += 1 #next greed
#             i += 1 #next cookie
#         return count