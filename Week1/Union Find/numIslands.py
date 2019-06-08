#Note that UnionFind solution is inherently more verbose than other approaches

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        numRows, numCols = len(grid), len(grid[0])
        uf = UnionFind(numRows, numCols)
        for row in range(numRows):
            for col in range(numCols):
                self.checkAround((row, col), grid, uf)
        hasOne = [coord for coord in uf.returnResult() if grid[coord[0]][coord[1]] == '1'] 
        return len(hasOne)
        
    def checkAround(self, coord, grid, uf):
        row, col = coord[0], coord[1]
        if col - 1 >= 0: #check left
            if grid[row][col - 1] == '1' and grid[row][col] == '1':
                uf.union((row, col), (row, col - 1))
        if row - 1 >= 0: #check above
            if grid[row - 1][col] == '1' and grid[row][col] == '1':
                uf.union((row, col), (row - 1, col))
        
          
class UnionFind:
    def __init__(self, numRows, numCols):
        self.parent, self.size = dict(), dict()
        for row in range(numRows):
            for col in range(numCols):
                self.parent[(row, col)] = (row, col)
                self.size[(row, col)] = 1
    def find(self, coord):
        if self.parent[coord] == coord:
            return coord
        self.parent[coord] = self.find(self.parent[coord]) #recurse & path compress
        return self.parent[coord]
    def union(self, coord1, coord2):
        root1 = self.find(coord1)
        root2 = self.find(coord2)
        if root1 == root2:
            return #don't union
        if self.size[root1] < self.size[root2]:
            #merge group1 into group2
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            #merge group2 into group1
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
    def returnResult(self):
        #flatten all & add roots to set
        return set(self.find(coord) for coord in self.parent)