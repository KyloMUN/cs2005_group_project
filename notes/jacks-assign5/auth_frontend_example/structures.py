"""Structures

Shared classes that creates objects used throughout the application.
"""

#import shortuuid
import datetime


def _new_id():
    return "123abc" # will uncomment for real application
    #return shortuuid.uuid()


class User:
    def __init__(self, username: str, password: str, role: str, realname: str = None):
        """Create a User.

        Keyword arguments:
        username -- users system name
        password -- password for the user
        role -- the initial role of the user
        realname -- optional real name for the user
        """
        self.username = username
        self.password = password
        self.roles = [role]
        self.realname = realname

        self.id = _new_id()
        self.classes = []
        self.question_banks = []


    def is_role(self, role: str) -> bool:
        """Return true if the user is the given role

        Keyword arguments:
        role -- role to verify if is User instance
        """
        return role in self.roles


class Quiz:
    def __init__(self, name: str, attempts_permitted: int = 1):
        """Create a Quiz.

        Keyword arguments:
        name -- name of the quiz
        attempts -- number attempts permitted, defaults to 1
        """
        self.name = name
        self.attempts_permitted = attempts_permitted

        self.id = _new_id()
        self.questions = []
        self.start_time = None
        self.end_time = None
        self.time_limit = None
        self.submitted = False
        self.permitted = []


class Class:
    """Create Class objects."""
    def __init__(self, classname: str, teacher: str):
        """Create a Class.

        Keyword arguments:
        classname -- the name of the class
        teacher -- teacher teaching the class
        """
        self.classname = classname
        self.teacher = teacher

        self.id = _new_id()
        self.students = []
        self.quizzes = []


class Question:
    def __init__(self, display: str):
        """Create a Question.

        Keyword arguments:
        display -- text to display
        """
        self.display = display

        self.id = _new_id()
        self.answers = {}
        self.choices = {}
        self.picked = []
        self.allowed_selections = allowedselections
        self.points = value


    def is_answer(self, key: str) -> bool:
        """Return true if the given key is an answer

        Keyword arguments:
        key -- key to verify if is answer
        """
        return key in self.answers


class QuestionBank:
    def __init__(self):
        """Create a QuestionBank."""
        self.id = _new_id()
        self.questions = []
