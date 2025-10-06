def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return None  # or raise an error if preferred
    return num % divisor == 0



# 1. check_divisibility(10, 2)

# Output: True (10 is divisible by 2)

# 2. check_divisibility(7, 3)

# Output: False (7 is not divisible by 3)
