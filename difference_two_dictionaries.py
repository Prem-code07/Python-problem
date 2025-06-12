# Program to find the difference of two dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
difference = {k: dict1[k] for k in dict1 if k not in dict2}
print("Difference (keys in dict1 not in dict2):", difference)
