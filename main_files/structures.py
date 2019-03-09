import shortuuid
import datetime

def new_id():
    return shortuuid.uuid()

class User:
    """Creates User objects."""
    def __init__(self, username, password, role, realname=None):
        """Create a Person.

        username -- users system name
        password -- password for the user
        role -- the initial role of the user
        realname -- optional real name for the user
        """
        self._id = id()
        self._username = username
        self._password = password
        self._role = [role]
        self._realname = realname

        self._classes = []

    def get_id(self):
        """Returns the users ID."""
        return self._id

    def get_username(self):
        """Returns the users system name."""
        return self._username

    def get_password(self):
        """Returns the users password."""
        return self._password

    def get_role(self):
        """Returns the users role."""
        return self._role

    def get_realname(self):
        """Returns the users real name."""
        return self._realname

    def get_classes(self):
        """Returns the users classes."""
        return self._classes

    def set_username(self, new_username):
        """Sets the users name.

        new_username -- new system username for the user
        """
        self._username = new_username

    def set_password(self, new_password):
        """Sets the users password."""
        self._password = new_password

    def add_role(self, new_role):
        """Add role to the user.

        new_role -- new role for the user
        """
        # TODO VERIFY NOT ALREADY IN ROLE
        self._role.append(new_role)

    def remove_role(self, role_to_remove):
        """Remove role from the user.

        role_to_remove -- role to remove from the user
        """
        self._classes.remove(role_to_remove)

    def set_realname(self, new_realname):
        """Sets the users real name.

        new_realname -- new real name for the user
        """
        self._realname = new_realname

    def add_class(self, new_class):
        """Add class to the user.

        new_class -- new class to add to the user
        """
        # TODO VERIFY NOT ALREADY IN CLASS
        self._classes.append(new_class)

    def remove_class(self, class_to_remove):
        """Remove class from the user.

        class_to_remove -- class to remove from the user
        """
        self._classes.remove(class_to_remove)


class Quiz:
    """Creates Quiz objects."""
    def __init__(self, name, attempts_permitted=1):
        """Create a Quiz.

        name -- name of the quiz
        attempts -- number attempts permitted, defaults to 1
        """
        self._id = new_id()
        self._attempts_permitted = attempts_permitted

        self._questions = []
        self._start_time = None
        self._end_time = None
        self._time_limit = None
        self._submitted = False

class Class:
    """Create a Class objects."""

    def __init__(self, classname):
        """Create a Class.

        classname -- the class identifier
        """
        self._id = new_id()
        self._classname = classname

        self._students = []
        self._quizzes = []
        self._teachers = []

class Question:
    """Create Question objects."""
    def __init__(self, display):
        self.id = new_id()
        self.display = display

        self.answers = {}
        self.choices = {}
        self.picked = []
        self.allowed_selections = allowedselections
        self.points = value

    def get_id(self):
        """Returns the Questions ID."""
        self._

    def get_answers(self):
        """Returns all answers to the question"""
        return self._answers

    def is_answer(self, key):
        """Returns true if the given key is an answer"""
        return key in self._answers

    def (self):
        """
        --
        """
        self._

    def (self):
        """
        --
        """
        self._

    def (self):
        """
        --
        """
        self._

    def (self):
        """
        --
        """
        self._

    def (self):
        """
        --
        """
        self._

    def (self):
        """
        --
        """
        self._

