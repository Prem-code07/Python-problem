def frequency_count(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

def most_common(lst):
    freq = frequency_count(lst)
    max_freq = max(freq.values())
    return [key for key, value in freq.items() if value == max_freq]

# Example
numbers = [1, 2, 2, 3, 3, 3]
print("Most Common:", most_common(numbers))
