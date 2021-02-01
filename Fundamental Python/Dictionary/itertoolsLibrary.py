import itertools

options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}

keys = list(options.keys())
values = [options[key] for key in keys]

print(values)
print(list(itertools.product(*values)))