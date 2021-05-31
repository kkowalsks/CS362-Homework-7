import fizzbuzz

def test_print():
    assert fizzbuzz.numbers(17) == True

def test_three():
    assert fizzbuzz.numbers(9) == "Fizz"