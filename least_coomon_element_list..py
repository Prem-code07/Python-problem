def least_common(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    min_freq = min(freq.values())
    return [key for key, value in freq.items() if value == min_freq]

# Example
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Least Common:", least_common(numbers))
