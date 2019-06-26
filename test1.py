from addition import *
from subtraction import *
from multiplication import *
from division import *
from testfunc import *


def main():
    add_result = addition(10, 20)
    test_equal("Addition", add_result, 30)

    sub_result = subtraction(60, 20)
    test_equal("Subbtraction", sub_result, 40)

    mul_result = multiplication(40, 50)
    test_equal("Multiplication", 2000)

    div_result = division(60, 2)
    test_equal("Division", 30)


if __name__ == '__main__':
    main()
