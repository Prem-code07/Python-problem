def count_substrings(s):
    n = len(s)
    return n * (n + 1) // 2  # Total substrings formula

# Example
text = "abcd"
print("Number of substrings:", count_substrings(text))
