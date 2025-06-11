def shortest_word(sentence):
    words = sentence.split()
    return min(words, key=len)

# Example
text = "Python programming is fun"
print("Shortest word:", shortest_word(text))
