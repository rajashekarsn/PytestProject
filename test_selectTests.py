import pytest

'''
The -r options accepts a number of characters after it, with a used above meaning “all except passes”.
Full list of available characters that can be used:
f - failed 
E - error 
s - skipped 
x - xfailed 
X - xpassed 
p - passed 
P - passed with output 
a - all except pP 
A - all 
More than one character can be used, so for example to only see failed and skipped tests, you can execute:
$ pytest -rfs


pytest -x            # stop after first failure
pytest --maxfail=2    # stop after two failures
pytest -x --pdb   # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3  # drop to PDB for first three failures
pytest test_selectTests.py::test_xfail #To run a specific test within a module:
pytest test_selectTests.py  #Run tests in a module
pytest PythonProjectTest/ #Run tests in a directory
pytest --pyargs pkg.testing #Run tests from packages

pytest --markers    # lists all markers
pytest test_selectTests.py -m skip
pytest test_selectTests.py -m xfail

'''

@pytest.fixture
def error_fixture():
    print ("FixtureError is called")
    assert 0

 #custom marker not setup
'''
@pytest.mark.testok
# content of pytest.ini
[pytest]
markers =
    testok: mark a test as a testok.
'''
def test_ok():
    print ("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    print("this statement is not read")
    pass


@pytest.mark.skip
def test_skip():
    pytest.skip("skipping this test")


@pytest.mark.xfail
def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass