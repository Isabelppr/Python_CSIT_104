# Example 5: Reducing the output of Pi
import math

pi_value = math.pi
print("Original value of Pi:", pi_value)  # Outputs 3.141592653589793

# Limiting the decimal places using format
print("Pi to 2 decimal places: {:.2f}".format(pi_value))  # Outputs 3.14
print("Pi to 4 decimal places: {:.4f}".format(pi_value))  # Outputs 3.1416

# Explanation:
# - You can control the number of decimal places displayed using string formatting.
# - This is useful for representing float values more concisely.
