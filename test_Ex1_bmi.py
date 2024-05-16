import Lab2.bmi as BMI


def test_bmi_normal(): 
    assert(BMI.calculate_bmi(1.60, 50)==0)


def test_bmi_over(): 
    assert(BMI.calculate_bmi(1.60, 90)==1)


def test_bmi_under(): 
    assert(BMI.calculate_bmi(1.60, 30)==-1)
