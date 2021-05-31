def numbers(x):
    check = False
    for i in range(1, 101):
        print(i)
        if i == x:
            check = True
    return check

numbers(17)