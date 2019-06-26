from functions.addition import addition
from functions.subtraction import subtraction
from functions.multiplication import multiplication
from functions.division import division
from functions.gen_str import gen_str
from functions.gen_list import gen_list
from functions.judge_value import judge_value
from testfunc import test, test_equal, test_not_equal, TestFailedException


def main():
    add_result = addition(10, 20)
    test_equal("Addition", add_result, 30)

    sub_result = subtraction(60, 20)
    test_equal("Subbtraction", sub_result, 40)

    mul_result = multiplication(40, 50)
    test_equal("Multiplication", 2000)

    div_result = division(60, 2)
    test_equal("Division", 30)

    gen_str_result = gen_str("Hello", "World!")
    test_equal("Generate Str", gen_str_result, "HelloWorld!")

    gen_list_result = gen_list(1, 5)
    test_equal("Generate List", gen_list_result, [1, 1, 1, 1, 1])

    judge_result = judge_value(10, 20)
    test("Judge Value", not judge_result)


if __name__ == '__main__':
    main()
