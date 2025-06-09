n = int(input("Enter n: "))
sum_odd = 0

for i in range(n):
    sum_odd += 2 * i + 1

print("Sum of first", n, "odd numbers is:", sum_odd)
