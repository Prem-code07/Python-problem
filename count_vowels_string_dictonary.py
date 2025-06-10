def count_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    for char in s:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1
    return vowel_count

# Example
text = "Hello World"
print("Vowel Count:", count_vowels(text))
