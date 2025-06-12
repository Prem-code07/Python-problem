# Program to check if a value exists
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = 2
if value in my_dict.values():
    print(f"Value '{value}' exists in dictionary.")
else:
    print(f"Value '{value}' does not exist in dictionary.")
