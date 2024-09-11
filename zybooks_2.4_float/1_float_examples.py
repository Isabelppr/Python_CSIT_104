# Example 1: Basic floating-point numbers
temperature = 98.6
small_number = 0.0001
negative_number = -666.667

print("Temperature:", temperature)  # Outputs 98.6
print("A small number:", small_number)  # Outputs 0.0001
print("A negative number:", negative_number)  # Outputs -666.667

# Explanation:
# - Floating-point numbers are numbers with decimal points.
# - They can represent a wide range of values, including very small or negative numbers.


# Example 2: Floating-point literals
value1 = 1.0  # A float with a fractional part of 0
value2 = 0.0
value3 = 99.0

print("Value 1:", value1)  # Outputs 1.0
print("Value 2:", value2)  # Outputs 0.0
print("Value 3:", value3)  # Outputs 99.0

# Explanation:
# - Even if the fractional part is 0, numbers with a decimal are considered floats.
# - This helps to differentiate them from integers.


# Example 3: Scientific notation
avogadro_number = 6.02e23  # Represents 6.02 * 10^23
small_value = 1.2e-4  # Represents 1.2 * 10^-4

print("Avogadro's number:", avogadro_number)  # Outputs 6.02e+23
print(type(avogadro_number))
print("A small value in scientific notation:", small_value)  # Outputs 0.00012

# Explanation:
# - Scientific notation is used to represent very large or very small numbers.
# - 'e' represents "times ten to the power of".
