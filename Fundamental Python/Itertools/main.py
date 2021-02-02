""" 
*** Iterator is defined as object types which contains values that can be accessed or iterated using a loop. 

*** Must-read: https://docs.python.org/3/library/itertools.html

- iter() 
    + returns an iterator for the given object

- next()
    + returns the next item from the iterator

- itertools.cycle()
    + Make an iterator returning elements from the iterable and saving a copy of each.
    + ex: cycle('ABCD') --> A B C D A B C D....

- itertools.dropwhile(predicate, iterable)
    + Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element.

- itertools.permutations(iterable, r=None)
    + r: the desire length
    + ex:   # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
            # permutations(range(3)) --> 012 021 102 120 201 210
    + NOTE: The permutation tuples are emitted in lexicographic ordering according to the order of the input iterable. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

- itertools.islice(iterable, start, stop[, step])
    + Make an iterator that returns selected elements from the iterable.
    + If stop is *None*, then iteration continues until the iterator is exhausted, if at all; otherwise, it stops at the specified position.

- itertools.combinations(iterable, r)
    + Return r length subsequences of elements from the input iterable.
    + NOTE: is similar with *permutations*

- itertools.combinations_with_replacement(iterable, r)
    + Return r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
    + ex: combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    + NOTE: is similar with *permutations*

- EXERCISES: 
    + ./CodeSignal/memoryPills.py
    + ./CodeSignal/cyclicName.py
    + ./CodeSignal/floatName.py
    + ./CodeSignal/kthPermutations.py
    + ./CodeSignal/crackingPassword.py
    + ./CodeSignal/crazyBall.py

"""

from itertools import cycle, dropwhile, count, takewhile, combinations, product, permutations, combinations_with_replacement

a = 'linhnt'
c = iter(a)
b = [(next(c)) for i in range(len(a))]
print(b)

d = cycle(a)
print(d, type(d), type(next(d)))

pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]
filteredPills = dropwhile(lambda s: len(s) % 2 != 0, pills)

print(next(filteredPills))

start = 0.1
stop = 1.6
step = 0.2

#lst = [start + start*i for i in count()]
# print(lst)

players = ["warrior", "trainee", "ninja"]
gen = permutations(players, 2) # tuple pairs
ans = list(gen)
print(type(ans[0]))
print(ans)

# 
numbers = [1, 2, 3, 4, 5]
ans = list(permutations(numbers, 5))
print(ans)
print(list(ans[3]))

# 
players = ["Ninja", "Warrior", "Trainee", "Newbie"]
ans = list(combinations(players, 3))
print(sorted(ans))

# 
print('\n\n\n-------------------------\n')
digits= [1, 5, 2]
def createString(d):
    return ''.join(map(str, d))

ans = [createString(x) for x in list(product(digits, repeat=2)) if int(createString(x)) % 3 == 0] 
print(ans)