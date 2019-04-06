import unittest
from authentication import Authentication
from structures import User

class FakePersist:
    def __init__(self):
        self.structure = None
        self.structure_instance = None
        self.structure_id = None
        self.custom_retrieve_value = None

    def store(self, structure):
        self.structure = structure

    def retrieve(self, structure, structure_id):
        self.structure = structure
        self.structure_id = structure_id

        if self.custom_retrieve_value:
            return self.custom_retrieve_value


class TestAuthentication(unittest.TestCase):
    def test_authentication_init(self):
        auth = Authentication(FakePersist())
        self.assertIsNotNone(auth)

    def test_authentication_add_user(self):
        fake_persist = FakePersist()
        auth = Authentication(fake_persist)
        auth.add_user('foobar', 'baz', 'professor')
        self.assertIsInstance(fake_persist.structure, User)

    def test_authentication_add_user_twice_fail(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz', 'student')
        self.assertDictEqual(auth.add_user('foobar', 'baz', 'student'), {})

    def test_authentication_login(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz', 'professor')
        self.assertDictEqual(auth.login('foobar', 'baz'), {})

    def test_authentication_login_wrong_password_fail(self):
        auth = Authentication(FakePersist())
        auth.add_user('wobble', 'spam', 'student')
        self.assertDictEqual(auth.login('wobble', 'wrong_password'), {})

    def test_authentication_login_unknown_user_fail(self):
        auth = Authentication(FakePersist())
        self.assertDictEqual(
            auth.login('foobar', 'baz'),
            {'success': False, 'message': 'User does not exist.'}
        )

    def test_authentication_change_password(self):
        auth = Authentication(FakePersist())
        auth.add_user('foobar', 'baz', 'student')
        auth.login('foobar', 'baz')
        self.assertDictEqual(auth.change_password('foobar', 'qux'), {})

    def test_authentication_change_password_fail(self):
        fake_persist = FakePersist()
        fake_persist.custom_retrieve_value = {}
        auth = Authentication(fake_persist)
        auth.add_user('foobar', 'baz', 'student')
        self.assertDictEqual(auth.change_password('foobar', 'qux', 'wobble'), {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
