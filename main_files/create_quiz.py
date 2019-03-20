"""This interacts with the Quiz and Question objects. Class CreateQuiz.

creates a new quiz object with the default attributes defined in the Quiz
object class. Methods to add the start time, end time, time limit and
questions to the quiz are provided in this class.
"""
import datetime
# from storage import Quiz, Question \
#causes erroring when uncommented
import shortuuid


class Create:
    """Interface for quiz creation."""

    def __init__(self, quizname, num_of_attempts):
        """Create a quiz object."""
        self.quiz = Quiz(quizname, num_of_attempts)
        pass

    def add_start_time(self, year, month, day, hour=None, minutes=None):
        """Allow authorized user to add the quiz start time.

        year -- int
        month -- int
        day -- int
        hour -- int
        minutes -- int
        """
        pass

    def add_end_time(self, year, month, day, hour=None, minutes=None):
        """Allow authorized user to add the quiz end time.

        year -- int
        month -- int
        day -- int
        hour -- int
        minutes -- int
        """
        pass

    def add_time_limit(self, minutes):
        """Allow authorized user to add a quiz time limit."""
        pass

    def pass_to_storage(self):
        """Pass a quiz object to persistance for storage."""
        pass

    def add_question(self, questiontext, points, answerdict, choicesdict,
                     display=None):
        """Stub implementation of adding a question object to quiz.

        questiontext -- string of question
        points -- int, value of question
        answerdict -- the set of answers
        choicesdict -- the set of choices
        display -- string
        """
        pass

    # methods relating to question bank

    def add_all_quiz_questions_to_bank(self, qbank):
        """Add all the questions from this quiz to the question bank for this course.

        course_id -- course uuid
        """
        pass

    def add_random_question_from_bank_to_quiz(self, qbank):
        """Get a random question from the question bank and add it to the quiz.

        course_id -- course uuid
        """
        pass

    def add_question_to_bank(self, qbank, questionobj):
        """Add a question to the question bank of this course id.

        course_id -- course uuid
        """
        pass
