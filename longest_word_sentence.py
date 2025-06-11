def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
text = "Python programming is fun"
print("Longest word:", longest_word(text))
