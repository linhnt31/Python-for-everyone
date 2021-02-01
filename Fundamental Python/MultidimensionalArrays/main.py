# list is mutable
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst[0] = [100, 101, 102]
print(lst)
print(lst[0], type(lst[0]))

