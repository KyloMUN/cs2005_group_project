import datetime

class Quiz:
    """Creates a new quiz object."""

    def __init__(self, numofattempts, starttime, endtime, timelimit=None):
        """Create a quiz object.

        targetstudents -- list of users who can take the quiz
        numofattempts -- int
        finalweight -- int
        starttime -- datetime timedelta
        endtime -- datetime timedelta
        timelimit -- datetime timedelta
        """
        self._questions = {}
        self._numofattempts = numofattempts
        self._starttime = starttime
        self._endtime = endtime
        self._timelimit = timelimit
        self._questionnumber = len(self._questions)

    def add_new_question(self, questionobj):
        """
        Add a new question object to the question list.

        Params:
            questionobj - a question object
        """
        self._questions[(questionobj._getquestionid] = questionobj

    def remove_question(self, questionid):
        """
        Remove the question at position questionNumber.

        Params:
            questionnumber - int
        """
        

    def get_num_of_attempts(self):
        """Return the number of attempts allowed."""
        return self._numofattempts

    def modify_num_of_attempts(self, newnumber):
        """
        Modify how many attempts can be had, unless start time is past.

        Params:
            newnumber - int
        """
        self._numofattempts = newnumber

    def get_final_weight(self):
        """Return the final weight."""
        return self._finalweight

    def modify_final_weight(self, newfinalweight):
        """
        Modify the quiz value on final grade.

        Params:
            newfinalweight - int
        """
        self._finalweight = newfinalweight

    def get_start_time(self):
        """Return the start time."""
        return self._starttime

    def modify_start_time(self, year, month, day, hour=None, minutes=None):
        """
        Allow authorized user to modify the quiz start time.

        Params:
            year - int
            month - int
            day - int
            hour - int
            minutes - int
        """
        self._starttime = datetime.datetime(year, month, day, hour, minutes)

    def get_end_time(self):
        """Return the end time."""
        return self._endtime

    def modify_end_time(self, year, month, day, hour=None, minutes=None):
        """
        Allow authorized user to modify the quiz end time.

        Params:
            year - int
            month - int
            day - int
            hour - int
            minutes - int
        """
        self._endtime = datetime.datetime(year, month, day, hour, minutes)

    def get_time_limit(self):
        """Return the time limit."""
        return self._timelimit

    def modify_time_limit(self, newtimeamount):
        """Allow authorized user to modify the quiz duration.

        This is a stub implementation (may not use timedelta)

        newtimeamount -- time in minutes.
        """
        self._timelimit = datetime.timedelta(newtimeamount)

    def is_available(self):
        if datetime.datetime.now() > self._starttime and datetime.datetime.now() < self._endtime:
            return True
        else:
            return False


class Question:
    """Parent class of all question types.

    Supports True and False by default.
    """

    def __init__(self, questiontext, correctanswer, displaytext=None):
        """
        Create a question object.

        questiontext -- a string of text
        correctans -- a string of text
        """
        self._question_id = shortuuid.uuid()
        self._questiontext = questiontext
        self._answers = {'correctanswer':}

    def get_question_id(self):
        """Return question uuid."""
        return self._question_id

    def get_question_text(self):
        """Return the questions text as a string."""
        return self._questiontext

    def accept_multiple_answers(self, answerkey, display=None):
        """Append new answer into the list of correct answers.
        answerkey -- the correct
        explanation -- an explanation of why the answer is right
        """
        self._answers[answerkey] = {"display": display}

    def remove_an_answer(self, invalid, replacement=None):
        """Allow quiz maker to remove or remove an answer.

        invalid -- string
        replacement -- string
        """
        pass


class MultipleChoice(Question):
    """Create a multiple choice question object."""

    def __init__(self, listofoptions):
        """Create multiple choice question object.

        numberofoptions -- int
        """
        self._listofoptions = listofoptions

    def add_option(self, newoption):
        """Add a new option to list of options.

        newoption -- string
        """
        self._listofoptions.append(newoption)


class FillInTheBlank(Question):
    """Create a fill in the blank question."""

    def __init__(self, wordbank):
        """Create fill in the blank question object.

        wordbank -- list
        """
        self._wordbank = wordbank
        for words in self._wordbank:
            words.toUpper()  # @jack does this work

    def add_single_to_wordbank(self, newword):
        """Add a single string to wordbank.

        new -- string
        """
        self._wordbank.append(newword)
        
