def second_smallest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[1] if len(unique) >= 2 else None

# Example
numbers = [4, 1, 2, 4, 3]
print("Second Smallest:", second_smallest(numbers))
