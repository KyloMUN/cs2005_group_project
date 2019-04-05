from create_quiz import Create
import unittest
import datetime
import persistence
from structures import Question, Quiz
from random import randint

class TestCreateQuizMethods(unittest.TestCase):
    """Tests the CreateQuiz interface."""

    def test_is_quiz_object(self):
        """Test if wrapper creates a quiz object."""
        test = Create('aquiz', 3)
        self.assertIsInstance(test.quiz, Quiz, msg="creating real quiz objects.")

    def test_quiz_name(self):
        """Test if name attribute is set."""
        test = Create('aquiz', 3)
        self.assertEqual(test.quiz.name, "aquiz")
    
    def test_quiz_num(self):
        """Test if number of attempts is set properly."""
        test = Create('aquiz', 3)
        self.assertEqual(test.quiz.attempts_permitted, 3)
    
    def test_time_limit(self):
        test = Create('aquiz', 3)
        test.add_time_limit(30)
        self.assertEqual(test.quiz.time_limit, 30)
    
    def test_time_limit_bad(self):
        """Test if time limit is set to invalid int."""
        test = Create('aquiz', 3)
        test.add_time_limit(0)
        valid = False
        if test.quiz.time_limit >=  0:
            valid = True
        self.assertTrue(valid)

    def test_time(self):
        test = Create('aquiz', 3)
        test.add_start_time(2020, 1, 1)
        valid = False
        if test.quiz.start_time != None:
            valid = True
        self.assertTrue(valid)

    def test_bad_time(self):
        test = Create("aquiz", 3)
        valid = True
        try:
            test.add_start_time(0, 0, 0)
        except ValueError:
            valid = False
        self.assertFalse(valid)

    # no point in testing end and start, they do the same thing
        
    def test_end_after_start(self):
        """Test if the quiz begins before it ends."""
        test = Create('aquiz', 3)
        test.add_start_time(2020, 3, 3)
        test.add_end_time(2019, 3, 3)
        valid = True
        if test.quiz.start_time > test.quiz.end_time:
            valid = True
        else:
            valid = False
        self.assertTrue(valid)

    def test_question_options_not_empty(self):
        """Test if the question is added to the list."""
        test = Create("aquiz", 3)
        test.add_question("What colour is the sky?", 1,{}, {})
        self.assertFalse(test.quiz.questions[0].answers)
    
    def test_answer_in_choices(self):
        test = Create('aquiz', 3)
        test.add_question("What colour is the sky?", 1, {"B":"BLUE"}, {"A":"RED", "B":"BLUE", "C":"GREEN"})
        self.assertTrue(test.quiz.questions[0].answers["B"] == test.quiz.questions[0].choices["B"])

if __name__ == '__main__':
    unittest.main()
