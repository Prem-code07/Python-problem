import itertools

def string_combinations(s):
    combos = []
    for i in range(1, len(s)+1):
        combos.extend([''.join(c) for c in itertools.combinations(s, i)])
    return combos

# Example
text = "abc"
print("Combinations:", string_combinations(text))
