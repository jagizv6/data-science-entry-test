def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list):
        return None
    return [replace_val if item == find_val else item for item in lst]



# 1. find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)

# Replaces all 2s with 5.
# Output: [1, 5, 3, 4, 5, 5]

# 2. find_and_replace(["apple", "banana", "apple"], "apple", "orange")

# Replaces all "apple" with "orange".
# Output: ["orange", "banana", "orange"]
