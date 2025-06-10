def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# Example
numbers = [1, 2, 3, 4, 5]
print("Product:", product_of_list(numbers))
