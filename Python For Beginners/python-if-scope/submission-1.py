def pay_bill(balance: int, bill: int) -> int:
    if balance >= bill:
        newb = balance - bill
        return newb

    else:
        return balance



# do not modify below this line
print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))
