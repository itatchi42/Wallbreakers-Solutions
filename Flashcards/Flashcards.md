# Python Notes

## Contents

- [Data Structures](#Data Structures)
- [Sorting](#Sorting) 



## Data Structures

### Lists:

#### Sort w/ Lambda

```python
lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x : x[1])
print(lst)
```

#### Binary Search

Bisect is Python's build-in binary search algorithm that returns insertion point to maintain sorted order of list. It assumes the list is **sorted**.

``` python
import bisect
a = [1,2,4,5] # missing 3
bisect.bisect(a, 3) # returns [index] 2
bisect.bisect_left(a, 2) # returns 1
bisect.bisect_right(a, 2) # returns 2
bisect.bisect(a, 2) # returns 2
```



### Heaps:

**O(1)** lookup find-max for max heaps, **O(logn)** deletion of max, and **O(logn)** node insertion. 



### Binary Search Trees:

**O(logn)** insertion, deletion, lookups, find-min, find-max, when tree is height-balanced.

*Height Balanced* means the height difference b/t the left and right subtrees is <= 1. Ex:![img](https://media.geeksforgeeks.org/wp-content/uploads/tree.jpg)



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

Below, 2 is still the pivot. Since 10 > 2, we shift the pivot left and perform the swap again. The resultant array looks like `[0, 3, 1, 7, 2, 10, 8 ]`.

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





