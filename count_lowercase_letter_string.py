def count_lowercase(s):
    return sum(1 for char in s if char.islower())

# Example
text = "Hello World"
print("Lowercase letters:", count_lowercase(text))
