# Problems to Remember

## Arrays

### Largest Number (Medium)

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

