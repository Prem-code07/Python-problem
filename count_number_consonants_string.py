def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Example
text = "Hello World"
print("Number of Consonants:", count_consonants(text))
