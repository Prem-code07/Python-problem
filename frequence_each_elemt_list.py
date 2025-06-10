def frequency_count(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Example
numbers = [1, 2, 2, 3, 3, 3]
print("Frequency Count:", frequency_count(numbers))
