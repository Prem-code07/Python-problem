a=input("Enter a string : ")
b=a.lower()
vowels="aeiou"
s=0
for i in b:
    if i in vowels:
        s+=1
print(f"The total vowels in the string is {s}")