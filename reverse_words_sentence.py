def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Example
text = "Python is fun"
print("Reversed words:", reverse_words(text))
