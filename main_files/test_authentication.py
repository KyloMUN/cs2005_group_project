import unittest
from authentication import Authentication
from structures import User

class FakePersist:
    def __init__(self):
        self.structure = None
        self.structure_instance = None
        self.structure_id = None


    def store(structure):
        self.structure = structure


    def retrive(structure, structure_id):
        self.structure = structure
        self.structure_id = structure_id


class TestAuthentication(unittest.TestCase):
    def test_authentication_init(self):
        auth = Authentication(FakePersist())
        self.assertIsNotNone(auth)


    def test_authentication_add_user(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz')
        self.assertIsInstance(User, FakePersist.structure)


    def test_authentication_add_user_twice_fail(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz')
        self.assertRaises(ValueError, auth.add_user('foobar', 'baz'))


    def test_authentication_login(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz')
        self.assertIsInstance(dict, auth.login('foobar', 'baz'))


    def test_authentication_login_wrong_password_fail(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz')
        self.assertIsInstance(dict, auth.login('foobar', 'wrong_password'))


    def test_authentication_login_unknown_user_fail(self):
        auth = Authentication(FakePersist())
        self.assertIsNone(auth.login('foobar', 'baz'))


    def test_authentication_change_password(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz')
        auth.login('foobar', 'baz')
        self.assertIsInstance(dict, auth.change_password('foobar', 'qux'))


    def test_authentication_change_password_fail(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz')
        auth.login('wrong', 'account')
        self.assertRaises(ValueError, auth.change_password('foobar', 'qux'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
