import datetime
import shelve


class Quiz:
    """Creates a new quiz object."""

    def __init__(self, targetstudents, numofattempts, finalweight,
                 starttime, endtime, timelimit=None):
        """
        Create a quiz object.

        Params:
            targetstudents - list of users who can take the quiz
            numofattempts - int
            finalweight - int
            starttime - datetime timedelta
            endtime - datetime timedelta
            timelimit - datetime timedelta
        """
        self._questionset = []
        self._targetstudents = targetstudents
        self._numofattempts = numofattempts
        self._finalweight = finalweight
        self._starttime = starttime
        self._endtime = endtime
        self._timelimit = timelimit

    def get_question_set(self):
        """Return the question set as a list."""
        return self._questionset

    def add_new_question(self, questionobj):
        """
        Add a new question object to the question list.

        Params:
            questionobj - a question object
        """
        self._questionset.append(questionobj)

    def remove_question(self, questionnumber):
        """
        Remove the question at position questionNumber.

        Params:
            questionnumber - int
        """
        del self._questionset[questionnumber-1]  # indexing starts at 0

    def get_target_students(self):
        """Return the target student group."""
        return self._targetstudents

    def modify_target(self, newtargetgroup):
        """
        Allow authorized user to change who is intended to take the quiz.

        Params:
            newtargetgroup - list
        """
        self._targetstudents = newtargetgroup

    def get_num_of_attempts(self):
        """Return the number of attempts allowed."""
        return self._numOfattempts

    def modify_num_of_attempts(self, newnumber):
        """
        Modify how many attempts can be had, unless start time is past.

        Params:
            newnumber - int
        """
        self._numOfattempts = newnumber

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
        """
        Allow authorized user to modify the quiz duration.

        This is a stub implementation (may not use timedelta)
        
        Params:
            newtimeamount - time in minutes.
        """
        self._timelimit = datetime.timedelta(newtimeamount)


class Question:
    """
    Parent class of all question types.

    Supports True and False by default.
    """

    def __init__(self, questiontext, correctans):
        """
        Create a question object.

        Params:
            questiontext - a string of text
            correctans - a string of text
        """
        self._questiontext = questiontext
        self._correctans = [correctans.toUpper()]

    def get_question_text(self):
        """Return the questions text as a string."""
        return self._questiontext

    def accept_multiple_answers(self, newacceptableanswer):
        """Append new answer into the list of correct answers."""
        self._correctans.append(newacceptableanswer.toUpper())

    def remove_an_answer(self, invalid, replacement=None):
        """
        Allow quiz maker to remove or remove an answer.

        Params:
            invalid - string
            replacement - string
        """
        if replacement is not None:
            self._correctans.append(replacement.toUpper())
        self._correctans.remove(invalid)


class MultipleChoice(Question):
    """Create a multiple choice question object."""

    def __init__(self, listofoptions):
        """
        Create multiple choice question object.

        Params:
            numberofoptions = int
        """
        self._listofoptions = listofoptions

    def add_option(self, newoption):
        """
        Add a new option to list of options.

        Param:
            newoption - string
        """
        self._listofoptions.append(newoption)


class FillInTheBlank(Question):
    """Create a fill in the blank question."""

    def __init__(self, wordbank):
        """
        Create fill in the blank question object.

        Params:
            wordbank - list
        """
        self._wordbank = wordbank
        for words in self._wordbank:
            words.toUpper()  # @jack does this work

    def add_single_to_wordbank(self, newword):
        """
        Add a single string to wordbank.

        Params:
            new - string
        """
        self._wordbank.append(newword)

    def add_list_to_wordbank(self, listofwords):
        """
        Add a list of words to wordbank.

        Params:
            listofwords - list
        """
        for words in listofwords:
            self._wordbank.append(words.toUpper())
