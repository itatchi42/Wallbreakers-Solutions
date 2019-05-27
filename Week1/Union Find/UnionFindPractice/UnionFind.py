class UnionFind:
	def __init__(self, n):
		self.parent = [x for x in range(n)]
		self.size = [1 for x in range(n)]

	def find(self, nodeNum):
		#path compression
		#once i find the parent, set each child's parent to this parent
		if self.parent[nodeNum] == nodeNum:
			return nodeNum
		self.parent[nodeNum] = self.find(self.parent[nodeNum])
		return self.parent[nodeNum]

	def union(self, nodeNum1, nodeNum2):
		#Find root nodes and update the parent array
		root1 = self.find(nodeNum1)
		root2 = self.find(nodeNum2)
		
		if root1 == root2:
			return #do nothing
		if self.size[root1] < self.size[root2]:
			#merge group1 into group2
			self.parent[root1] = root2
			self.size[root2] += self.size[root1]
		else:
			#merge group2 into group1
			self.parent[root2] = root1
			self.size[root1] += self.size[root2]

	def printParent(self):
		print("index: ",list(range(9)))
		print("parent: ", self.parent, sep='')


uf = UnionFind(9)
uf.union(2,1)
uf.union(4,3)
uf.union(6,5)
print("\nParent array after union(2,1), union(4,3) and union(6,5):")
uf.printParent()

# Part b)
uf.union(2,4)
print("\nParent array after union(2,4)")
uf.printParent()

# Part c)
uf.find(3)
print("\nParent array after find(3)")
uf.printParent()

#Part d)
uf.union(5, 1)
print("\nParent array after union(5, 1)")
uf.printParent()

# Part e)
myDict = {}
for node in range(9):
	root = uf.find(node)
	if not root in myDict:
	    myDict[root] = set([node])
	else:
		myDict[root].add(node)
print("\nDisjoint sets: ")
for mySet in myDict.values():
	print(mySet)