def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

num = int(input("Enter the number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += factorial(digit)
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")
