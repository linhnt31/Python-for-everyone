# Ref: https://www.geeksforgeeks.org/deque-in-python/

""" Deque
- belongs to the module **collections**
- is preferred over **list** --> when we need **quicker append and pop operations** from both 2 ends.
- Time complexity: O(1) 
"""

from collections import deque

# Declaring a deque
dq = deque(['ling', 'min', 'hp'], 0)
print(dq, type(dq), len(dq))

dq.rotate(-1)

print(dq)