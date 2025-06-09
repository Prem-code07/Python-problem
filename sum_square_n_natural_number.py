n = int(input("Enter n: "))
sum_squares = 0

for i in range(1, n+1):
    sum_squares += i**2

print("Sum of squares of first", n, "natural numbers is:", sum_squares)
