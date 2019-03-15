"""Structures

Shared classes that creates objects used throughout the application.
"""

#import shortuuid
import datetime


def _new_id():
    return "123abc" # will uncomment for real application
    #return shortuuid.uuid()


class User:
    def __init__(self, username, password, role, realname=None):
        """Create a User.

        Keyword arguments:
        username -- users system name
        password -- password for the user
        role -- the initial role of the user
        realname -- optional real name for the user
        """
        self.id = _new_id()
        self.username = username
        self.password = password
        self.role = [role]
        self.realname = realname

        self.classes = []
        self.question_banks = []


class Quiz:
    def __init__(self, name, attempts_permitted=1):
        """Create a Quiz.

        Keyword arguments:
        name -- name of the quiz
        attempts -- number attempts permitted, defaults to 1
        """
        self.id = _new_id()
        self.attempts_permitted = attempts_permitted

        self.questions = []
        self.start_time = None
        self.end_time = None
        self.time_limit = None
        self.submitted = False


class Class:
    """Create Class objects."""
    def __init__(self, classname):
        """Create a Class.

        Keyword arguments:
        classname -- the class identifier
        """
        self._id = _new_id()
        self._classname = classname

        self._students = []
        self._quizzes = []
        self._teachers = []


class Question:
    def __init__(self, display):
        """Create a Question.

        Keyword arguments:
        display -- text to display
        """
        self.id = _new_id()
        self.display = display

        self.answers = {}
        self.choices = {}
        self.picked = []
        self.allowed_selections = allowedselections
        self.points = value

    def is_answer(self, key):
        """Return true if the given key is an answer

        Keyword arguments:
        key -- key to verify if is answer
        """
        return key in self.answers
