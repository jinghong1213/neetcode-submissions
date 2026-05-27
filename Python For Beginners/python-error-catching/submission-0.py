def divide_numbers(a: str, b: str) -> None:
    try:
        num1 = int(a)
        num2 = int(b)
        print(num1/num2)
    
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
