import unittest
from persistence import Persistence
from structures import User, Quiz, Class, Question, QuestionBank

# Persistence creates a singleton,
# therefore it is useless to define multiple of these variables.
storage = Persistence()

class TestPersistence(unittest.TestCase):
    def test_persistence_init(self):
        self.assertIsNotNone(storage._shelf)

    def test_persistence_init_fail(self):
        test_persist = Persistence('foo')

        with self.assertRaises(OSError, msg='Should throw OSError on trying to create two references to one shelve'):
            Persistence('foo')

    def test_persistence_store_user(self):
        new_user = User('foobar', 'baz', 'student')
        storage.store(new_user)
        same_user = storage.retrieve(User, new_user.id)
        self.assertIsNotNone(same_user)
        self.assertIsInstance(same_user, User)

    def test_persistence_retrive_user_fail(self):
        invalid_id = 'abc123'
        user = storage.retrieve(User, invalid_id)
        self.assertIsNone(user)

    def test_persistence_store_quiz(self):
        new_quiz = Quiz('foobar', 10)
        storage.store(new_quiz)
        same_quiz = storage.retrieve(Quiz, new_quiz.id)
        self.assertIsNotNone(same_quiz)
        self.assertIsInstance(new_quiz, Quiz)

    def test_persistence_retrive_quiz_fail(self):
        invalid_id = 'abc123'
        quiz = storage.retrieve(Quiz, invalid_id)
        self.assertIsNone(quiz)


if __name__ == '__main__':
    unittest.main(verbosity=2)
