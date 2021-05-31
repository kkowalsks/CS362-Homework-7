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
            if int % 400 != 0:
                int = str(int)
                print(int + " is not a leap year")
                return False
            else:
                int = str(int)
                print(int + " is a leap year")
                return True

leapCheck(2020)
leapCheck(2021)
leapCheck(1900)
leapCheck(2000)