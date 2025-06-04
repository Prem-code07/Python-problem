numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
total = sum(numbers)
print(f"The sum of the list is: {total}")
