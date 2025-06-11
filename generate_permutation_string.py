import itertools

def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# Example
text = "abc"
print("Permutations:", string_permutations(text))
