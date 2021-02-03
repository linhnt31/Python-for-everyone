""" zip(iterables)
- aggregates iterables in a *tuple*
- If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.

- Ref: https://www.programiz.com/python-programming/methods/built-in/zip
    + ./CodeSignal/pressureGauges.py
"""

num_lst = [1, 2, 3]
str_lst = ['one', 'two', 'three']
fl_lst = [4.1, 4.2, 4.3]

res1 = zip()
res2 = zip(num_lst)
res3 = zip(num_lst, str_lst, fl_lst)

print(list(res1)) # []
print(list(res2)) # [(1,), (2,), (3,)]
print(list(res3)) # [(1, 'one'), (2, 'two'), (3, 'three')]