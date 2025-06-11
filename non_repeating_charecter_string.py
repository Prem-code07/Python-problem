def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# Example
text = "aabbcde"
print("First non-repeating character:", first_non_repeating_char(text))
