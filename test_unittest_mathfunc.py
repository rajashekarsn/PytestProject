import mathfunc
import pytest

'''
Running pytest can result in six different exit codes:
Exit code 0:	All tests were collected and passed successfully
Exit code 1:	Tests were collected and run but some of the tests failed
Exit code 2:	Test execution was interrupted by the user
Exit code 3:	Internal error happened while executing tests
Exit code 4:	pytest command line usage error
Exit code 5:	No tests were collected

run at terminal
pytest.py -v #verbose
pytest - v test_unittest_mathfunc.py  #Run tests in a module

'''



def test_add():
    assert mathfunc.add2int(2, 3) == 5
    assert mathfunc.add2int(2) == 4


def test_mul():
    assert mathfunc.mul2int(2, 4) == 8
    assert mathfunc.mul2int(2) == 6
    assert mathfunc.mul2int(2, 3) == 4


def test_add_strings():
    assert mathfunc.add2int("Hello", " World") == "Hello World"

