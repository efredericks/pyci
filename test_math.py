import mathlib

def test_calc_addition():
    output = mathlib.calc_addition(2,4)
    assert output == 6

 

def test_calc_substraction():
    output = mathlib.calc_substraction(2, 4)
    assert output == -2

     

def test_calc_multiply():
    output = mathlib.calc_multiply(2,4)
    assert output == 8

def test_calc_multiply2():
    output = mathlib.calc_multiply(2,4)
    assert output == 16
