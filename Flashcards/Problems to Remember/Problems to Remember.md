# Problems to Remember

## Arrays

### Largest Number (Medium)
[Problem](https://www.interviewbit.com/problems/largest-number/)
Given a list of non negative integers, arrange them such that they form the largest number. For example:
Given `[3, 30, 34, 5, 9]`, the largest formed number is `9534330`.

```python
from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = map(str, A) # Conv to iterable-only map
        # Create comparator func to sort by comparing two strings at time
            # Return 1 if True, -1 if False, 0 if Equal
        key = cmp_to_key(lambda a, b : 1 if a+b > b+a else -1) 
            # Note: Can only compare strings of same len
        A = sorted(A, key = key, reverse = True)
        ans = ''.join(A)
        if '0' * len(A) == ans: return '0'
        return ans
```

### Hotel Bookings Possible (Medium)
[Problem](https://www.interviewbit.com/problems/hotel-bookings-possible/)

A hotel manager has to process `N` advance bookings of rooms for the next season. His hotel has `K` rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. For example:
arrive: `[1, 2, 3, 4, 5]`
depart: `[2, 6, 8, 14, 15]`
K: 2
	-> Returns *False*, since there are three overlapping dates: (2, 3, 4)

```python
class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        # Concept: If K+1 consecutive dates overlap, return False
            # Key: Soln assumes both arrays sorted!
        arrive.sort() # O(nlogn)
        depart.sort()
        if len(arrive) - K < 0: return True # Less guests than rooms avail
        for x in range(len(arrive) - K):
            if arrive[x+K] < depart[x]:
                return False
        return True
```







