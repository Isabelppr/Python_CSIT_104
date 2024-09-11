# Example 4: Using Modulo to Get the Last Digit
number = 12345
last_digit = number % 10
print("Last digit of 12345 is:", last_digit)  # Outputs 5

# Example 5: Using Modulo and Floor Division to Get Digits
second_last_digit = (number // 10) % 10
print("Second last digit of 12345 is:", second_last_digit)  # Outputs 4

# Explanation:
# - To get the last digit, use % 10.
# - To get other digits, use a combination of floor division (//) and modulo (%).

# Example 6: Extracting Prefix Using Floor Division
full_number = 123456
prefix = full_number // 1000  # Removes the last three digits
print("Prefix of 123456 is:", prefix)  # Outputs 123

# Example 7: Identifying Even or Odd Numbers
number = 42
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")  # Outputs "42 is even."

# Explanation:
# - Floor division (//) is useful for getting a truncated number or extracting a prefix.
# - Modulo (%) helps determine properties like even or odd by checking remainders.
