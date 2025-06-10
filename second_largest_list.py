def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# Example
numbers = [4, 1, 2, 4, 3]
print("Second Largest:", second_largest(numbers))
