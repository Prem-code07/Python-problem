def recursive_product(lst):
    if not lst:
        return 1
    return lst[0] * recursive_product(lst[1:])

# Example
numbers = [1, 2, 3, 4, 5]
print("Product:", recursive_product(numbers))
