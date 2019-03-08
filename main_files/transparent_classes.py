import shortuuid
import datetime

class Person:
    """Public class for person objects."""

    def __init__(self, realname, username, password, role):
        """Create a person object.

        username -- string
        password -- string
        role -- string
        """
        self.name = fullname
        self.id = shortuuid.uuid()
        self.username = username
        self._password = password
        self.role = [role]
        self.classes = []

    def _verify_password(self, testpassword):
        """Check stored password against testpassword string.

        testpassword -- string
        """
        if testpassword == self._password:
            return True
        return False

    # get methods

    def get_name(self):
        """Return persons name."""
        return self.name

    def get_role(self):
        """Return role."""
        return self.role

    def get_username(self):
        """Get username."""
        return self.id

    def get_id(self):
        """Get ID."""
        return self.id

    def get_classes(self):
        """Return classlist."""
        return self.classes

    # change methods

    def change_username(self, newusername, password):
        """Change username."""
        if self._verify_password(password):
            self.username = newusername
        else:
            raise Exception("Bad password; nothing changed.")

    def change_password(self, oldpassword, newpassword):
        """Change password."""
        if self._verify_password(oldpassword):
            self._password = newpassword
        else:
            raise Exception("Bad password; nothing changed")

    def change_role(self, newrole):
        """Change role."""
        self.role = newrole

    # add methods

    def add_role(self, newrole):
        """Add a role to role list."""
        self.role.append(newrole)

    def add_class(self, newclassid):
        """Add a class to class list."""
        self.classes.append(newclassid)


class Quiz:
    """Create Quiz object."""

    def __init__(self, quizname, numberofattempts):
        """Attributes of Quiz object."""
        self.id = shortuuid.uuid()
        self._questions = []
        self.num_of_attempts = numberofattempts
        self.start_time = None
        self.end_time = None
        self.time_limit = None

    # set methods

    def set_time_limit(self, duration):
        pass
    
    def set_start_time(self, year, month, day, hour, minute):
        """Set a start time."""
        self.start_time = datetime.datetime(year, month, day, hour, minute)

    def set_end_time(self, year, month, day, hour, minute):
        """Set an end time."""
        self.end_time = datetime.datetime(year, month, day, hour, minute)

    # get methods

    def get_id(self):
        return self.id
    
    def get_questions(self):
        return self._questions
    
    def get_num_of_attempts(self):
        return self.num_of_attempts

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_time_limit(self):
        return self.time_limit

    # change methods

    def change_num_of_attempts(self, newnumberofattempts):
        self.num_of_attempts = newnumberofattempts

    def change_time_limit(self):
        pass

    def change_start_time(self, year, month, day, hour, minute):
        self.start_time = datetime.datetime(year, month, day, hour, minute)
    
    def change_end_time(self, year, month, day, hour, minute):
        self.end_time = datetime.datetime(year, month, day, hour, minute)


class Class:
    """Create a Class object."""

    def __init__(self, classname):
        self.classname = classname
        self.students = []
        self.quizzes = []
        self.id = shortuuid.uuid()
        self.teachers = []

    # set methods

    def set_teacher(self, teacherobj):
        """Save teacher as a dictionary of Name, Attributes."""
        self.teachers.append({teacherobj.get_id(): teacherobj})
    
    def set_students(self, listofstudents):
        """Set student list as a list of student objects."""
        self.students = listofstudents
    
    # add methods

    def add_student(self, student):
        self.students.append(student)
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)
    
    # remove methods

    def remove_student(self, student):
        templist = []
        for stu in self.students:
            if stu.get_id() != student.get_id():
                templist.append(stu)
        self.students = templist

    def remove_teacher(self, teacher, newteacher=None):
        templist = []
        for tea in self.teachers:
            if tea.get_id() != teacher.get_id():
                templist.append(tea)
        if len(self.templist) == 0 and newteacher=None:
            raise Exception("You must assign a new teacher to this class.")
            self.teachers = self.teachers
        else:
            self.teachers = templist

    def remove_quiz(self, quiz):
        templist = []
        for qui in self.quizzes:
            if qui.get_id() != quiz.get_id():
                templist.append(qui)
        self.quizzes = templist
    
    # get methods

    def get_teachers(self):
        return self.teachers
    
    def get_students(self):
        return self.students
    
    def get_classname(self):
        return self.classname
    
    def get_id(self):
        return self.id
    
    def get_quizzes(self):
        return self.quizzes

class Question:

    def __init__(self, questiontext, allowedselections, value, displaytext=None):
        self.id = shortuuid.uuid()
        self.display = displaytext
        self.answers = {}
        self.choices = {}
        self.picked = []
        self.allowed_selections = allowedselections
        self.points = value
