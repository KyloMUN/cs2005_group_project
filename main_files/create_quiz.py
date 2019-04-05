"""create_quiz.py

This interacts with the Quiz and Question objects. Class CreateQuiz
creates a new quiz object with the default attributes defined in the Quiz
object class. Methods to add the start time, end time, time limit and
questions to the quiz are provided in this class.
"""
import datetime
from persistence import Persistence
from structures import Question, QuestionBank, Quiz


class Create:
    """This module is a wrapper for the Quiz object. This module creates
    a new quiz, and the methods to add the start time, end time, time
    limit and questions to the quiz are provided in this class.
    """

    def __init__(self, quizname, num_of_attempts):
        """This method initializes a new Quiz object with the basic
        attributes, a name and the number of alloted attempts. This is
        done by calling the Quiz class in structure.py, and giving it the
        quizname and num_of-attempts attributes in this method. It then
        creates a self.quiz variable that will be used to refer to the
        quiz in further methods. As well, an instance of persistance is
        created to store the quiz.

        quizname: String
        num_of_attempts: Int
        """
        self.quiz = Quiz(quizname, num_of_attempts)
        self.question_bank = QuestionBank()
        self.persist = Persistence()

    def add_start_time(self, year, month, day, hour=0, minutes=0):
        """This method allows a quiz object to be given a start time,
        in the form of a datetime.datetime() object. This is done by
        calling this method with the above parameters, which will be
        used to make the datetime.datetime() object. This method then
        updates the start time attribute of the quiz object, so that the
        quiz is only available after this date passes.

        year: Int
        month: Int
        day: Int
        hour: Int
        minutes: Int
        """
        self.quiz.start_time = datetime.datetime(year, month, day, hour, minutes)

    def add_end_time(self, year, month, day, hour=0, minutes=0):
        """This method allows a quiz object to be given a end time,
        in the form of a datetime.datetime() object. This is done by
        calling this method with the above parameters, which will be
        used to make the datetime.datetime() object. This method then
        updates the end time attribute of the quiz object, so that the
        quiz is no longer available after this date passes.

        year: Int
        month: Int
        day: Int
        hour: Int
        minutes: Int
        """
        self.quiz.end_time = datetime.datetime(year, month, day, hour, minutes)

    def add_time_limit(self, minutes):
        """This method sets the time limit attribute of a quiz object. This is
        done by taking the paramatar minutes and setting the attribute time
        limit of a quiz to a value in minutes, so that when the quiz is started,
        a timer is started equal to this value.

        minutes: Int
        """
        self.quiz.time_limit = minutes

    def pass_to_storage(self):
        """This method uses the store() method of the persistence module to
        store the quiz. This method stores the object regardless of whether
        every attribute is set or not, thus allowing quiz modification in
        the future."""
        self.persist.store(self.quiz)

    def get_id(self):
        """Returns the ID of the quiz currently being created"""
        return self.quiz.id

    def add_question(self, questiontext, points, answerdict, choicesdict):
        """This method is a wrapper for the Question class in the structures
        module. It sets attributes of a question, which are filled by the user
        by the highlighted parameters.

        questiontext: String
        points: Int
        answerdict: {"DisplayOfAnswer":"Answer"}
        choicesdict: {"DisplayA": "ChoiceA", "DisplayB": "ChoiceB", "DiplayC": "ChoiceC"}
        """
        myquestion = Question(questiontext, points)
        myquestion.answers = answerdict
        myquestion.choices = choicesdict

        self.quiz.questions.append(myquestion)

    def add_all_questions_to_bank(self):
        """This method adds all questions in the quiz to a question bank, then
        stores the bank in persistence.
        """
        for question in self.quiz.questions:
            self.question_bank.questions.append(question)

        self.persist.store(self.question_bank)

    def get_random_question_from_bank(self, course_id):
        """Add a random question from the bank to the quiz."""
        qbank = self.persist.retrieve(QuestionBank, course_id)
        return qbank[randint(0, len(qbank)-1)]
