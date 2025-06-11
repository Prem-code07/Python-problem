def count_digits(s):
    return sum(1 for char in s if char.isdigit())

# Example
text = "My number is 12345"
print("Number of digits:", count_digits(text))
