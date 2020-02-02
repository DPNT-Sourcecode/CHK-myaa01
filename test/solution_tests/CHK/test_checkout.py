from solutions.CHK import checkout_solution


class TestCheckout():
    def test_illegal_input(self):
        """ Reject inputs that contain any letter that is not one of A,B,C,D,E """
        assert checkout_solution.checkout('ABCDEFGZ') == -1
        assert checkout_solution.checkout('J') == -1
        assert checkout_solution.checkout('abcd') == -1
        assert checkout_solution.checkout('__*&^TBN') == -1
        assert checkout_solution.checkout('123') == -1

    def test_empty_input(self):
        assert checkout_solution.checkout('') == 0

    def test_singular_skus(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_multiple_priced_skus(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 200
        assert checkout_solution.checkout('AAAAAAAA') == 330
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('BBB') == 75

    def test_special_offers_combination(self):
        assert checkout_solution.checkout('EE') == 80
        assert checkout_solution.checkout('BEE') == 80
        assert checkout_solution.checkout('BBEE') == 110
        assert checkout_solution.checkout('BBBEE') == 125
        assert checkout_solution.checkout('F') == 10
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 30


