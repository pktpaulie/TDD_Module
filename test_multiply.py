"""Using the pytest method for unit testing"""


from multiply import multiply


def test_multiply():
    """calling the assertEqual function"""

    assert multiply(2, 2) == 4
