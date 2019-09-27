# Python Notes

## Contents

- [Primitive Types](#Primative Types)
- [Data Structures](#Data Structures)
- [Sorting](#Sorting) 



## Primitive Types

### Strings:

#### ASCII Characters

```python
val = ord('a') # val = 97
letter = chr(val) # letter = 'a'
```

#### Convert String to List

```python
myStr = 'abcdef'
myList = list(myStr) # ['a', 'b', 'c', 'd', 'e', 'f']
```





## Data Structures

### 2D Arrays:

You can implement a 2D array very easily w/ a dict, for example:

```python
arr2D = dict()
arr2D[0, 0] = 5
arr2D[0, 1] = 5
```





### Lists:

#### Sort w/ Lambda

Allows you to specify the key that you wish to sort by.

```python
lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x : x[1]) # In-place sort
print(lst)
# Note: `sorted` returns list
```

#### Binary Search

Bisect is Python's build-in binary search algorithm that returns insertion point to maintain sorted order of list. It assumes the list is **sorted**. 

It's recommended to search using `bisect` rather than `find` or `index` in a sorted list.

``` python
import bisect
a = [1,2,4,5] # missing 3
bisect.bisect(a, 3) # returns [index] 2
bisect.bisect_left(a, 2) # returns 1
bisect.bisect_right(a, 2) # returns 2
bisect.bisect(a, 2) # returns 2
```





### Heaps:

A heap has property that ALL nodes follow particular order. A *max heap* means that every parent is BIGGER than its children. A *min heap* means that every parent is SMALLER than its children. 

Ex:

*Valid* min heap

![minheap_good](https://github.com/itatchi42/Wallbreakers-Solutions/blob/master/Flashcards/images/minheap_good.png)



*Invalid* min heap

![minheap_bad](https://github.com/itatchi42/Wallbreakers-Solutions/blob/master/Flashcards/images/minheap_bad.png)

**O(1)** lookup find-max for max heaps, **O(logn)** deletion of max, and **O(logn)** node insertion. 





### Priority Queues:





### Binary Search Trees:

**O(logn)** insertion, deletion, lookups, find-min, find-max, when tree is height-balanced.

*Height Balanced* means the height difference b/t the left and right subtrees is <= 1. Ex:![img](https://media.geeksforgeeks.org/wp-content/uploads/tree.jpg)





### Union Finds:

Structure that merges clusters of nodes together. Merges smaller cluster into larger cluster. 

When path compression is implemented, the complexity of the 'find' operation is **O(n)** and the complexity of the 'union' operation is also **O(n)**. 

#### Implementation

```python
class UnionFind:
  def __init__(self, x):
    self.children = [0 for num in range(x)]
    self.parent = list(range(x)) # Each node points to themself as parent
  def find(self, node):
    if self.parent[node] == node: # If pt to yourself (i.e., root)
      return node
    root = self.find(self.parent[node]) # Recurse up through parents 'till root
    self.parent[node] = root # Path compression
    return self.parent[node]
  def union(self, node1, node2):
    root1, root2 = self.find(node1), self.find(node2)
    if self.children[root1] > self.children[root2]: # merge group2 -> group1
      self.parent[root2] = root1
      self.children[root1] += self.children[root2]
    if self.children[root2] >= self.children[root1]: # merge group1 -> group2
      self.parent[root1] = root2
      self.children[root2] += self.children[root1] 
```





## Sorting

### Merge Sort

Split array into pairs of two elements and do atomic swaps. Then merge pairs together and sort the merged array. 

Complexity: **O(nlogn)**

#### Implementation

```python
# TODO: Implement merge sort here
```



### Quick Sort

Set a pointer to the last ele of the array and call it `pivot`. Set another pointer to the beginning of the array and call it `i`. Continue swapping them until everything to the left of pivot is < pivot value and everything to right is >= pivot value. 

Recursivey halve the array and repeat quick sort on each half.

Ex:

Here, 2 is the pivot. Since 8 > 2, we shift the pivot left and perform the swap.

![quicksort1](https://github.com/itatchi42/Wallbreakers-Solutions/blob/master/Flashcards/images/quicksort1.png)

Below, 2 is still the pivot. Since 10 > 2, we shift the pivot left and perform the swap again. After this step, the resultant array will look like `[0, 3, 1, 7, 2, 10, 8 ]`.

![quicksort2](https://github.com/itatchi42/Wallbreakers-Solutions/blob/master/Flashcards/images/quicksort1.png)

Complexity: **O(nlogn)**

#### Implementation

```python
# Tested. Works.
class soln:
    def quicksort(self, array, start, end):
        if end - start < 1: return
	i, pivot = start, end
	while i < pivot:
	    if array[i] > array[pivot]:
	    temp = array[i]
    	    array[i] = array[pivot - 1] # Swap values
 	    array[pivot - 1] = array[pivot] # Shift values
	    array[pivot] = temp
	    pivot -= 1 # Change pivot ptr
	    else: i+= 1

	self.quicksort(array, start, pivot-1) # LHS
	self.quicksort(array, pivot + 1, end ) # RHS, Don't include pivot b/c pivot is in right place
	return array
```





