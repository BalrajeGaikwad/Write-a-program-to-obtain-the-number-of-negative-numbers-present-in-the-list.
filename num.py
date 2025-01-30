"""

A list contains only positive and negative integers. Write a program to obtain the number of negative numbers present in the list."""

# List of integers (positive and negative)
numbers = [12, -5, 8, -7, -10, 6, -3]

# Initialize the count
negative_count = 0

# Count the negative numbers
for num in numbers:
    if num < 0:
        negative_count += 1

# Print the result
print("Number of negative numbers:", negative_count)
