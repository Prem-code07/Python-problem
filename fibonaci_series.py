def fibonnaci_series(n):
    if n<=0:
        print(f"{n} the is should be positive .")
    else:
        a,b=0,1
        for i in range(n):
            print(a,end=" ")
            a,b=b,a+b
n=int(input("Enter a number : "))
print(f"Fibbonaci series of {n} is : {fibonnaci_series(n)}")            
