def group_by_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1  # Count frequencies
    
    grouped = {}
    for key, value in freq.items():
        grouped.setdefault(value, []).append(key)  # Group by frequency
    
    return grouped

# Example
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Grouped by Frequency:", group_by_frequency(numbers))
