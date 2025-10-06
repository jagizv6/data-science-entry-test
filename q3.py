def update_dictionary(dct, key, value):
    if not isinstance(dct, dict):
        return None  # or raise an error if preferred

    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct


# 1. update_dictionary({}, "name", "Alice")

# Key "name" does not exist.
# Adds "name": "Alice" to the dictionary.
# Output: {'name': 'Alice'}

# 2. update_dictionary({"age": 25}, "age", 26)

# Key "age" exists with value 25.
# Prints: Original value for 'age': 25
# Updates "age" to 26.
# Output: {'age': 26}