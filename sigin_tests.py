import signin
import unittest


class UserLoginTestCase(unittest.TestCase):
    def setUp(self):
        signin.app.config['TESTING'] = True
        self.app = signin.app.test_client()

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username = username,
            password=password
        ),follow_redirects=True)

    def test_login_ok(self):
        rv = self.login("test", "test123")
        assert b'Success' in rv.data

    def test_login_not_ok(self):
        rv = self.login("test", "test")
        assert b'Fail' in rv.data

    def test_login_unknown_user(self):
        rv = self.login("batman", "test123")
        assert b'Fail' in rv.data

if __name__ == '__main__':
    unittest.main()
