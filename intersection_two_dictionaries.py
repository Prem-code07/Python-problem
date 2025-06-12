# Program to find the intersection (common keys) of two dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
intersection = {k: dict1[k] for k in dict1 if k in dict2}
print("Intersection (common keys):", intersection)
