num_list = []
q = True

while q is True:
    num = input("Give me a number: ")
    if num == "stop":
        break
    num_list.append(int(num))
    print(f"Your list is {num_list}")
    x = 0
    for i in num_list:
        x += i
    print(f"The sum of all numbers is {x}")
    
        