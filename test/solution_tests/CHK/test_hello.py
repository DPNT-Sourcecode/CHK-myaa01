import pytest

from solutions.CHK import checkout_solution


class TestCheckout():
    def test_illegal_input(self):
        assert checkout_solution.checkout('ABCDE')


