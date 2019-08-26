# Python Notes

## Contents

- [Lists](#Lists)
- [Sorting](Sorting) 



## Lists

### Sort w/ Lambda

```python
lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x : x[1])
print(lst)
```

### Binary Search

Bisect is Python's build-in binary search algorithm that returns insertion point to maintain sorted order of list. It assumes the list is **sorted**.

``` python
import bisect
a = [1,2,4,5] # missing 3
bisect.bisect(a, 3) # returns [index] 2
bisect.bisect_left(a, 2) # returns 1
bisect.bisect_right(a, 2) # returns 2
bisect.bisect(a, 2) # returns 2
```

##  

## Sorting

### Merge Sort

Split array into pairs of two elements and do atomic swaps. Then merge pairs together and sort the merged array. 

Complexity: **O(nlogn)**

#### Implementation

```python
# TODO: Implement merge sort here
```



### Quick Sort

Randomly pick a pivot. Use two pointers and continue swapping them until everything to the left of pivot is < pivot value and everything to right is >= pivot value. 

Recursivey halve the array and repeat quick sort on each half.

Complexity: **O(nlogn)**

#### Implementation

```python
# TODO: Implement quick sort here
```





