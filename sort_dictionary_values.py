my_dict = {'banana': 3, 'apple': 5, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_dict)
