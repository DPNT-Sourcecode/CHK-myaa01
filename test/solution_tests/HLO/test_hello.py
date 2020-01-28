from solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello('adam') == 'Hello, World!'
        assert hello_solution.hello('toby') == 'Hello, World!'



