import shelve
import datetime


class Quiz:
    """
    Creates a new quiz object.
    """
    def __init__(self, targetStudents, numOfAttempts, finalWeight,
                 startTime, endTime, timeLimit=None):
        self._questionSet = []
        self._targetStudents = targetStudents
        self._numOfAttempts = numOfAttempts
        self._finalWeight = finalWeight
        self._startTime = startTime
        self._endTime = endTime
        self._timeLimit = timeLimit

    def get_question_set(self):
        """
        Returns the question set as a list.
        """
        return self._questionSet

    def add_new_question(self, questionObj):
        """
        Adds a new question object to the question list.
        """
        self._questionSet.append(questionObj)

    def remove_question(self, questionNumber):
        """
        Removes the question at position questionNumber.
        """
        del self._questionSet[questionNumber-1]  # indexing starts at 0

    def get_target_students(self):  # run me by jack
        """
        Returns the target student group
        """
        return self._targetStudents

    def modify_target(self, newTargetGroup):
        """
        Allows authorized user to change who is intended to take the quiz.
        """
        self._targetStudents = newTargetGroup

    def get_num_of_attempts(self):
        """
        Returns the number of attempts
        """
        return self._numOfAttempts

    def modify_num_of_attempts(self, newNumber):
        """
        Modifies how many attempts can be had.
        Should check to see if start time has past already, and if it has deny
        the change.
        """
        self._numOfAttempts = newNumber

    def get_final_weight(self):
        """
        Returns the final weight
        """
        return self._finalWeight

    def modify_final_weight(self, newFinalWeight):
        """
        Allows authorized user to modify the quiz's value on final grade.
        """
        self._finalWeight = int(newFinalWeight)

    def get_start_time(self):
        """
        Returns the start time
        """
        return self._startTime

    def modify_start_time(self, year, month, day, hour=None, minutes=None):
        """
        Allows authorized user to modify the quiz start time.
        (This is more of quality of life as changing end time is already
        implemented.)
        """
        self._startTime = datetime.datetime(year, month, day, hour, minutes)

    def get_end_time(self):
        """
        Returns the end time.
        """
        return self._endTime

    def modify_end_time(self, year, month, day, hour=None, minutes=None):
        """
        Allows authorized user to modify the quiz end time.
        """
        self._endTime = datetime.datetime(year, month, day, hour, minutes)

    def get_time_limit(self):
        """
        Returns the time limit
        """
        return self._timeLimit

    def modify_time_limit(self, newTimeAmount):
        """
        Allows authorized user to modify the quiz duration.
        This is a stub implementation (may not use timedelta)
        """
        self._timeLimit = datetime.timedelta(newTimeAmount)


class CreateNewQuiz:
    """
    This is where a quiz is actually built by the user.
    """
    def create_new_quiz(self, quizName):
        """
        This is the main method that will call all other methods to create a
        quiz object.
        """
    answered = 0
    targetStudents = input("Which group will take this quiz? ")
    numOfAttempts = input("How many tries will they get? ")
    finalWeight = input("What percent of their final mark will this weight? ")
    startTime = input("This quiz will be available at: ")
    endTime = input("This quiz will no longer be available at: ")
    while answered is 0:
        yn = input("(Y/N) Would you like a time limit? ")
        if yn is "Y":
            timeLimit = input("In minutes, how long will the time limit be? ")
            quizName = Quiz(targetStudents, numOfAttempts, finalWeight,
                            startTime, endTime, timeLimit)
            answered = 1
        if yn is "N":
            quizName = Quiz(targetStudents, numOfAttempts, finalWeight,
                            startTime, endTime)
            answered = 1
        print("Type 'Y' or 'N'")

    class Question:
        """
        Parent class of all question types.
        """
        def __init__(self, questionText):
            self._questionText = questionText

        def get_question_text(self):
            """
            Returns a string formatted exactly as the quiz creator
            typed it.
            """
            return self._questionText
        
        def accept_multiple_answers(self, newAcceptableAnswer):
            """
            Allows user to create a list of acceptable answers instead.
            Handles case where quiz maker decides two answers are viable by
            merging the inital answer with the new one. Handles if quiz maker
            decides any number more are viable answers.

            If changed after quiz has been evaluated, quizzes will need to be
            reevaluated.

            self._correctAns can become a list in this case.
            """
            if isinstance(self._correctAns, list):
                self._correctAns.append(newAcceptableAnswer)
            ansList = []
            ansList.append(self._correctAns)
            ansList.append(newAcceptableAnswer)
            self._correctAns = ansList

        def remove_an_answer(self, invalid, newAnswer=None):
            """
            Allows quiz maker to remove an invalid answer, or change it to a
            new one.
            """
            isList = isinstance(self._correctAns, list)  # check if list
            if newAnswer is None:
                if isList:
                    self._correctAns.remove(invalid)
                else:
                    raise Exception("You must provide a new answer.")
            else:
                if isList:
                    place = self._correctAns.index(invalid)
                    self._correctAns[place] = newAnswer
                else:
                    self._correctAns = newAnswer

    class MultipleChoice(Question):
        """
        Creates a multiple choice question object.
        """
        def __init__(self, optionsABCD, correctAns):
            self._optionsABCD = optionsABCD
            self._correctAns = correctAns

        def get_correct_ans(self):
            """
            Returns a string containing a single, uppercased letter
            that is the answer to this question.
            """
            return self._correctAns.toUpper()

        def get_optionsABCD(self):
            """
            Returns a list of options, in the form [A, B, C, D].
            """
            return self._optionsABCD

    class FillInTheBlank(Question):
        """
        Creates a new question of type fill in the blank.
        """
        def __init__(self, correctAns):
            self._correctAns = correctAns

        def get_correct_ans(self):
            """
            Returns the correct answer in the form of a capitalized string.
            """
            return self._correct.toUpper()

    class TrueOrFalseQuestion(Question):
        """
        Creates a new question of type true or false.
        """
        def __init__(self, correctAns):
            self._correctAns = correctAns

        def get_correct(self):
            """
            Returns correct as an int, 0 for False or 1 for True.
            This is to avoid confusion with Pythons True and False.
            """
            return self._correct
