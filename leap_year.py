n=int(input("Enter year what you waint tyo check ; "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print(n, "is a leap year.")
else:
    print(n, "is not a leap year.")