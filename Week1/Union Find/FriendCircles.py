class Solution:
    size = []
    parent = []
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        global size, parent
        
        count = 0
        width = len(M)
        size = [1 for x in range(width)]
        parent = [x for x in range(width)]
        
        for i in range(width * width):
            #Conv 1D indx -> 2D
            x = i % width
            y = i // width
            #If not on diagonal
            if x != y:
                if M[x][y] == 1:
                    self.union(x, y)
        
        #path compress everything + get num. disjoint sets
        unique = set(self.find(val) for val in range(width))
        return len(unique)
        
            
    
    def union(self, num1, num2):
        global parent, size
        root1 = self.find(num1)
        root2 = self.find(num2)
        if root1 == root2:
            return #do nothing
        if size[root1] < size[root2]:
            #merge group 1 into group2
            parent[root1] = root2
            size[root2] += size[root1]
        else:
            #merge group2 into group1
            parent[root2] = root1
            size[root1] += size[root2]
        
    def find(self, num1):
        global parent
        #Break if found root
        if parent[num1] == num1: 
            return num1
        #Path compress and find root
        parent[num1] = self.find(parent[num1])
        return parent[num1]
            
            
