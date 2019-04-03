"""This interacts with the Quiz and Question objects. Class CreateQuiz
creates a new quiz object with the default attributes defined in the Quiz
object class. Methods to add the start time, end time, time limit and
questions to the quiz are provided in this class.
"""
import datetime
from persistence import Persistence
from structures import Question, Quiz, QuestionBank
from random import randint

class Create:
    """Interface for quiz creation."""

    def __init__(self, quizname, num_of_attempts):
        """Create a quiz object."""
        self.quiz = Quiz(quizname, num_of_attempts)
        self.persist = Persistence()

    def add_start_time(self, year, month, day, hour=0, minutes=0):
        """Allow authorized user to add the quiz start time.

        year -- int
        month -- int
        day -- int
        hour -- int
        minutes -- int
        """
        datetimetemp = datetime.datetime(year, month, day, hour, minutes)
        self.quiz.start_time = datetimetemp

    def add_end_time(self, year, month, day, hour=0, minutes=0):
        """Allow authorizsd user to add the quiz end time.

        year -- int
        month -- int
        day -- int
        hour -- int
        minutes -- int
        """
        datetimetemp = datetime.datetime(year, month, day, hour, minutes)
        self.quiz.end_time = datetimetemp

    def add_time_limit(self, minutes):
        """Allow authorized user to add a quiz time limit."""
        self.quiz.time_limit = minutes

    def pass_to_storage(self):
        """Pass a quiz object to persistance for storage."""
        self.persist.store(self.quiz)
        
    def add_question(self, questiontext, points, answerdict, choicesdict):
        """Stub implementation of adding a question object to quiz.

        questiontext -- string of question
        points -- int, value of question
        answerdict -- the set of answers
        choicesdict -- the set of choices
        """
        myquestion = Question(questiontext, points)
        myquestion.answers = answerdict
        myquestion.choices = choicesdict
        self.quiz.questions.append(myquestion)
        

    # methods relating to question bank
   
    def add_all_questions_to_bank(self):
        """Add a question to the question bank of this course id."""
        tempbank = []
        for questions in self.quiz.questions:
            tempbank.append(questions)
        Persistence.store(tempbank, QuestionBank)
    
    def get_random_question_from_bank(self, course_id):
        qbank = self.persist.retrieve(QuestionBank, course_id)
        return qbank[randint(0, len(qbank)-1)]
