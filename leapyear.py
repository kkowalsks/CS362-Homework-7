def leapCheck(int):
    if int % 4 != 0:
        int = str(int)
        print(int + " is not a leap year")
        return False
    else:
        if int % 100 != 0:
            int = str(int)
            print(int + " is a leap year")
            return True
        else:
            int = str(int)
            print(int + " is not a leap year")
            return False

leapCheck(2020)
leapCheck(2021)
leapCheck(1900)