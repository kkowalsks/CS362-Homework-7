import leapyear

def test_four():
    assert leapyear.leapCheck(2020) == True
    assert leapyear.leapCheck(2021) == False

def test_hundred():
    assert leapyear.leapCheck(1900) == False