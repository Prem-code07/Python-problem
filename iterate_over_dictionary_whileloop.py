# Program to iterate over dictionary using while loop
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = list(my_dict.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f"Key: {key}, Value: {my_dict[key]}")
    i += 1
