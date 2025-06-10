def remove_occurrences(lst, val):
    return [x for x in lst if x != val]

# Example
numbers = [1, 2, 3, 2, 4, 2]
print("List after removal:", remove_occurrences(numbers, 2))
