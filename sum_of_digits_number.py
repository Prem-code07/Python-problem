# Python program to calculate the sum of digits of a number

# Get user input
num = int(input("Enter a number: "))

# Initialize sum
sum_of_digits = 0

# Loop to extract digits and compute the sum
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

# Display the result
print("Sum of digits:", sum_of_digits)
