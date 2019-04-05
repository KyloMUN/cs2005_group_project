import unittest
from stub_quiz import Quiz, Question, MultipleChoice
from take_quiz import QuizInProgress, TakingQuiz
from persistence import Persistence
storage = Persistence()
q= Quiz(3)
c1 = MultipleChoice("question1", "one", ["one", "two", "three", "nine"])
c2 = MultipleChoice("question2", "two",["one", "two", "three", "four"])
c3 = MultipleChoice("question3", "three", ["one", "six", "three", "four"])
c4 = MultipleChoice("question4", "four", ["five", "two", "three", "four"])
c5 = MultipleChoice("question4", "four", ["five", "two", "three", "four"])
c1.set_quest_id(1)
c2.set_quest_id(2)
c3.set_quest_id(3)
c4.set_quest_id(4)
c5.set_quest_id(5)
mylist=[]
mylist.append(c1)
mylist.append(c2)
mylist.append(c3)
mylist.append(c4)
mylist.append(c5)
for i in mylist:
    q.addQuest(i)
qp = QuizInProgress()
qp.setQuizId("1111")
tq = TakingQuiz(qp)
class TestTakingQuiz(unittest.TestCase):
    def test_submit(self):
        tq.submit()
        self.assertTrue(tq._takingQuiz.getComplete())

    def test_submit_one(self):
        tq.submit()
        check=storage._shelf["QuizInProgress"]
        self.assertEqual(type(check["1111"]), QuizInProgress)
        
    def test_subm_fail(self):
        tq.submit()
        check=storage._shelf["QuizInProgress"]
        with self.assertRaises(KeyError):
                check["11111"] 
        
        

class TestTakeQuiz(unittest.TestCase):

    def test_setQuestion(self):
        qp.setQuestions()
        self.assertEqual(type(qp.getQuestions()), dict)

    def test_getQuizAnswer(self):
        self.assertEqual(type(qp.getQuizAnswer()), dict)
                        
    def test_loadQuiz(self):
        self.assertTrue(qp.loadQuiz(q))
        self.assertFalse(qp.loadQuiz(2))
        
    def test_get_quest_id(self):
        qp.loadQuiz(q)
        self.assertEqual(qp.get_quest_id(1), 2)

    def test_checkTimeLimit(self):
        qp.loadQuiz(q)
        self.assertTrue(qp.checkTimeLimit())

        
        
    def test_getQuestion(self):
        qp.loadQuiz(q)
        self.assertEqual(qp.getQuestionText(0), 'question1')
        self.assertEqual(qp.getQuestionText(1), 'question2')
        self.assertEqual(qp.getQuestionText(2), 'question3')
        self.assertEqual(qp.getQuestionText(3), 'question4')
        with self.assertRaises(IndexError):
            qp.getQuestionOptions(6)

    def test_getQuestionOptions(self):
        qp.loadQuiz(q)
        self.assertEqual(qp.getQuestionOptions(0), ["one", "two", "three", "nine"])
        self.assertEqual(qp.getQuestionOptions(1), ["one", "two", "three", "four"])
        self.assertEqual(qp.getQuestionOptions(2), ["one", "six", "three", "four"])
        self.assertEqual(qp.getQuestionOptions(3), ["five", "two", "three", "four"])
        with self.assertRaises(IndexError):
            qp.getQuestionOptions(7)

    def test_setAnswer(self):
        qp.loadQuiz(q)
        
        self.assertEqual(len(qp.getQuizAnswer()), 0)
            
    def test_incrAttempts(self):
        qp.loadQuiz(q)
        self.assertEqual(qp.attemps, 4)
        qp.incrAttempts()
    def test_incrAttempts_fail(self):
        self.assertNotEqual(qp.attemps, 6)

    
    def test_checkAttempts(self):
        qp.loadQuiz(q)
        qp.incrAttempts()
        self.assertTrue(qp.checkAttempts())
        qp.incrAttempts()
        qp.incrAttempts()
        qp.incrAttempts()
        self.assertFalse(qp.checkAttempts())

    def test_submit(self):
        qp.loadQuiz(q)
        self.assertFalse(qp.complete)
        qp.submit()
        self.assertTrue(qp.complete)


        
if __name__ == '__main__':
    unittest.main()
