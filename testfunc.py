class TestFailedException(Exception):
    pass


def test_equal(name, comp_a, comp_b):
    if comp_a != comp_b:
        raise TestFailedError(name)


def test_not_equal(name, comp_a, comp_b):
    if comp_a == comp_b:
        raise TestFailedError(name)


def test(name, bool_val):
    if not bool_val:
        raise TestFailedError(name)

