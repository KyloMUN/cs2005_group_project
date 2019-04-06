import datetime
from stub_quiz import Quiz, Question, MultipleChoice
from persistence import Persistence
storage = Persistence()
class TakingQuiz:
    '''Create TakingQuiz'''

    def __init__(self,  QuizInPr):
        self._takingQuiz = QuizInPr

        '''
        self._takingQuiz quiz in progress
         object of class QuizInProgress
        '''

    def _setComplete(self):
        '''
        set quiz as completed
        '''
        self._takingQuiz.setComplete()


    def submit(self):
        '''
         Submit quiz to persist storage

        '''
        self._setComplete()
        storage.store(self._takingQuiz)



    def pause(self):
        '''
      Pause quiz. Save to persist storage
        '''
        storage.store(self._takingQuiz)

class QuizInProgress:
    ''' Create new quiz in progress'''
    def __init__(self):
        '''

        quiz_id - id quiz
        quiz_in_progress - quiz is taking
        attemps - number of attempts
        quiz_answer - dict with key (id of question) value: students answer
        complete - checking if quiz is completed
        quest_set - dict with key question, values option for question
        '''

        self.id = ''
        self.quiz_in_progress = Quiz
        self.attemps = 0
        self.quiz_answer = {}
        self.complete = False

        self.quest_set= {}

    def getQuizId(self):
        '''
        returns id of quiz
        '''
        return self.id

    def setQuizId(self,newid):
        '''
        set id of quiz
        '''
        self.id=newid

    def getComplete(self):
        '''
        return complete status
        '''
        return self.complete

    def setComplete(self):
        '''
        set complete as true
        '''
        self.complete=True

    def getQuestions(self):
        '''returns a dict with of questions and options of answer '''
        self.setQuestions()
        return self.quest_set

    def setQuestions(self):
        '''Returns a dict with of questions and options of answer'''
        for i in self.quiz_in_progress.get_question_set():
            self.quest_set[i.getQuestionText()] = i.getOptions()
    def getQuizAnswer(self):
        ''' Returns quiz answers'''
        return self.quiz_answer

    def setAnswer(self, quest_id, answer):
        '''Adds answer to dict of answers

        parametrs:
        quest_id - id of a question
        answer
        '''
        quiz_answer[quest_id] = answer

    def get_quest_id(self, index):
        '''Return question id for each answer

        parametr:
        index
        '''
        return self.quiz_in_progress.get_question_set()[index].get_question_id()

    def loadQuiz(self, quiz):
        '''Load quiz from persist storage'''
        self.quiz_in_progress = quiz

        if (type(self.quiz_in_progress)==Quiz):
            return True
        else:
            return False
    def getQuestSize(self):
        '''Returns size of question list'''
        return len(self.quiz_in_progress.get_question_set())

    def getQuestionText(self, index):
        '''
        Return question text by index
        parametr: index
        '''
        if index > len(self.quiz_in_progress.get_question_set()):
            raise IndexError
        else:
            return self.quiz_in_progress.get_question_set()[index].getQuestionText()


    

    def getQuestion(self, index):

        '''
        Return question by index
        parametr: index
        '''
        
        return (str(self.getQuestionText(index)) + '\n'+ str(self.getQuestionOptions(index)))

    def getQuestionOptions(self, index):
        
        '''
        Return option of answer for question by index
        parametr: index
        '''
        if index > len(self.quiz_in_progress.get_question_set()):
            raise IndexError
        else:
            return self.quiz_in_progress.get_question_set()[index].getOptions()


 

    def incrAttempts(self):
        '''
         Increment number of attemps
        '''
        self.attemps +=1


    def checkAttempts(self):
        '''
        Checks number of attemps
        '''
        if self.attemps > self.quiz_in_progress.get_num_of_attempts():
            return False
        else:
            return True

    def submit(self):
        '''
         Submit quiz to persist storage
         
        '''
        
        self.complete = True

 
        
    def checkTimeLimit(self):
        '''
        Checks time limit
        '''
        return self.quiz_in_progress.is_available() 
        

