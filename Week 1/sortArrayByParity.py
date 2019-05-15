class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #step 1: use list comphrehension for even elements
        list1=[x for x in A if not x%2]
   
        #step 2: list comprehension for odd elements
        list2 = [x for x in A if x%2]
        
        #step 3: concat the two lists
        return list1+list2
        