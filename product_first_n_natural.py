n = int(input("Enter n: "))
product = 1

for i in range(1, n+1):
    product *= i

print("Product of first", n, "natural numbers is:", product)
