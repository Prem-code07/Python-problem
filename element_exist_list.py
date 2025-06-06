def check_element(list,element):
    if element in list:
        return True
    else:
        return False
a=[10,20,30,40,50]
b=30
if check_element(a,b):
    print(f"{b} is exist in the list .")
else:
     print(f"{b} is not exist in the list .")