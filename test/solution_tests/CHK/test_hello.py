from solutions.CHK import checkout_solution


class TestCheckout():
    def test_illegal_input(self):
        """ Reject inputs that contain any letter that is not one of A,B,C,D """
        assert checkout_solution.checkout('ABCDE') == -1
        assert checkout_solution.checkout('J') == -1
        assert checkout_solution.checkout('abcd') == -1
        assert checkout_solution.checkout('__*&^TBN') == -1
        assert checkout_solution.checkout('123') == -1




