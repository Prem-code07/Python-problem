def count_special_characters(s):
    return sum(1 for char in s if not char.isalnum() and not char.isspace())

# Example
text = "Hello@World!"
print("Special characters:", count_special_characters(text))
