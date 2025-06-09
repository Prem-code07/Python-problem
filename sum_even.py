n = int(input("Enter n: "))
sum_even = 0

for i in range(1, n+1):
    sum_even += 2 * i

print("Sum of first", n, "even numbers is:", sum_even)
