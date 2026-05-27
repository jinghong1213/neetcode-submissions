def add_two_numbers() -> int:
    user_input = input()
    strings = user_input.split(",")
    
    sum1 = 0

    for s in strings:
        sum1 += int(s)

    return sum1



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
