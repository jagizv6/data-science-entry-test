def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x = x + y
    y = x - y
    x = x - y
    print(f"Swapped values: x = {x}, y = {y}")

# 1. swap("Apple", 10)

# "Apple" is a string, not numeric.
# Output: -1

# 2. swap_values(9, 17)

# Both are integers.
# Swapping will result in: x = 17, y = 9
# Output: Swapped values: x = 17, y = 9