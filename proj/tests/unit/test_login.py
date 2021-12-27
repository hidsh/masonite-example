from tests.TestCase import TestCase


class Login(TestCase):
    def setUp(self):
        super().setUp()

    def test_loginにアクセスしたときにアクセスできる(self):
        assert self.get('/login')

