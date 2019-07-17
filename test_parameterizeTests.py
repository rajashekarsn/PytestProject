import mathfunc
import pytest


@pytest.mark.parametrize('num1,   num2,   result',
                         [
                             (7, 3, 10),
                             ("Hello ", "World", "Hello World"),
                             (2.2, 3.3, 5.5)
                         ]
                         )

def test_add(num1, num2, result):
    assert mathfunc.add2int(num1, num2) == result