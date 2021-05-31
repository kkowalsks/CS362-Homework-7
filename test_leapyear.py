import leapyear

def test_four():
    assert leapyear.leapCheck(2020) == True
    assert leapyear.leapCheck(2021) == False