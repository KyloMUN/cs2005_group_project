'''structures.py.

Shared classes that create objects used throughout the application. These
structures define the base for which most functions will be editing,
and are important to be decoupled as coupling could cause major errors within
the system.
'''
import shortuuid


def _new_id():
    return shortuuid.uuid()


class User:
    '''Defines the properties of a User within the system.'''

    def __init__(self, username: str, password: str, role: str,
                 realname: str = None):
        '''
        This initializes the User in the system, along with their username,
        password, real name, and which role they have whether it is the role of
        an instructor, administrator, or a student.

        Keyword arguments:
        username -- users system name
        password -- password for the user
        role -- the initial role of the user
        realname -- optional real name for the user
        '''
        self.username = username
        self.password = password
        self.roles = [role]
        self.realname = realname

        self.id = username
        self.classes = []
        self.question_banks = []

    def is_role(self, role: str) -> bool:
        '''Return true if the user is the role that is given to the function.
        This method is important for checking which users can do what, so that
        no student is able to do what they should not be able to do.

        Keyword arguments:
        role -- role to verify if is User instance
        '''
        return role in self.roles


class Quiz:
    '''Defines the properties of a Quiz, which professors can create and edit,
    and students can take.'''

    def __init__(self, name: str, attempts_permitted: int = 1):
        '''Initializes a quiz object. Along with initializing a quiz it also
        takes in the name of the quiz and the amount of attempts any student can
        have to take the quiz.

        Keyword arguments:
        name -- name of the quiz
        attempts -- number attempts permitted, defaults to 1
        '''
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
    '''Defines the properties of a Class professors can create and users can be
    enrolled in. Quizzes themselves are segregated by which class they are
    assigned to, so have a Class structure is important to not have quizzes and
    their respective attributes roll over into other classes.
    '''

    def __init__(self, classname: str, professor: str):
        '''Create a Class.

        Keyword arguments:
        classname -- the name of the class
        professor -- user teaching the class
        '''
        self.classname = classname
        self.professor = professor

        self.id = _new_id()
        self.students = []
        self.quizzes = []


class Question:
    '''Defines the properties of a Question, which professors can create and
    users can answer. Each quiz has a list of questions, and each question can
    be pulled from persistence and compared against answers by students.
    '''
    def __init__(self, display: str, points: int):
        '''
        Initializes a question, and takes in what the question is asking as it's
        display, as well as how many points the question will be graded with.

        Keyword arguments:
        display -- text to display
        '''
        self.display = display
        self.points = points

        self.id = _new_id()
        self.answers = {}
        self.choices = {}
        self.picked = []

    def is_answer(self, key: str) -> bool:
        '''This function returns true if the key that has been taken in is also
        in the list of answers. This is used as the primary way of determining
        if the answer a student provides is what the professor is looking for.

        Keyword arguments:
        key -- key to verify if is answer
        '''
        return key in self.answers


class QuestionBank:
    '''Defines the properties of a QuestionBank professors can create and refer
    to later.
    '''

    def __init__(self):
        '''Create a QuestionBank.'''
        self.id = _new_id()
        self.questions = []
