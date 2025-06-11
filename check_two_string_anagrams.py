def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example
print("Are anagrams:", are_anagrams("listen", "silent"))
