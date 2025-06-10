def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# Example
nested = [1, [2, [3, 4], 5], 6]
print("Flattened List:", flatten_list(nested))
