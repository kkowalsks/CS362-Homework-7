def numbers(x):
    check = False
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
            if i == x:
                check = "Fizz"
        else:
            print(i)
            if i == x:
                check = True

    return check

numbers(17)