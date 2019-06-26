class TestFailedException(Exception):
    pass


def test_equal(name, comp_a, comp_b):
    if comp_a != comp_b:
        raise TestFailedException(name)
    print(name + " : Success!")


def test_not_equal(name, comp_a, comp_b):
    if comp_a == comp_b:
        raise TestFailedException(name)
    print(name + " : Success!")


def test(name, bool_val):
    if not bool_val:
        raise TestFailedException(name)
    print(name + " : Success!")

