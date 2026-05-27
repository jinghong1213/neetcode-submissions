def add_two_numbers() -> int:
    user_input = input()
    strings = user_input.split(",")
    
    sum1 = 0

    for s in strings:
        sum1 += int(s)

    return sum1

    #line = input()
    #string_list = line.split(",")
    
    #num1 = int(string_list[0])
    #num2 = int(string_list[1])
    
    #return num1 + num2


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
