
import unittest
from resultAndgrade import Result, Grade
#import structures



class Test_Result_and_Grade(unittest.TestCase):


    question_list = ["question1","question2","question3","question4"]
    correct_ans=["a","b","c","d"]
    point_list=[1,1,1,1]  #full mark = 4
    answer_dict= {
        "student1": [["a","b","b","b"],["b","c","b","d"],["a","b","d","d"]],
        "student2": [],
        "student3": [["a","a","b","b"],["a","c","b","d"],["a","b","a","d"]],
        "student4": [["d","b","c","b"],["a","b","c","d"]]
    }
    grade_dict={
        "student1": [[1,1,0,0],[0,0,0,1],[1,1,0,1]],
        "student2": [],
        "student3": [[1,0,0,0],[1,0,0,1],[1,1,0,1]],
        "student4": [[0,1,1,0],[1,1,1,1]]        
    }
    #the good_data is read only
    good_data = [
                [[2,1,3],[],[1,2,3],[3,4]],  #good_data[0] is list of grade for all attempts for all students 
                [3,0,3,4]                          #good_data[1] is list of highest grade for students
                ]
    result = Result(answer_dict, point_list, question_list, 1, correct_ans)
    grade1 = result.get_student_grade_object("student1")
    grade2 = result.get_student_grade_object("student2")
    

    def test_calculate_fullmark(self):
        
        self.result.calculate_fullmark()
        a = self.result.getFullMark()
        self.assertEqual(4, a, msg="Full mark incorrect")

    def test_get_student_grade_object(self):
        
        self.assertTrue(isinstance(self.grade1, Grade), msg="It is not a Grade object")
    
    def test_make_result_dict(self):    
        self.result.make_result_dict()
        a = self.result.get_result_dict()    
        self.assertEqual(4, a["student4"],msg="The dictionary is incorrect")
    
    def test_calculate_Average(self):
        self.result.calculate_Average()
        a= self.result.getAverage()
        self.assertAlmostEqual(2.5, a, places=1, msg="The average is incorrect")

    def test_calculate_participation(self):  #also means check get_participation() method
        self.result.calculate_participation()
        a = self.result.get_participation()
        self.assertEqual(3, a, msg="The number of participation is incorrect")
    
    def test_calculate_grade(self):  #also means check getHighestGrade() method, because the grade of the quiz is the highest grade
        a=self.grade1.getHighestGrade()
        self.assertEqual(3,a,msg="the highest grade is calculated incorrectly")

    def test_calculate_empty_grade(self):
        a=self.grade2.getHighestGrade()
        self.assertEqual(0,a,msg="the highest grade is calculated incorrectly")

    def test_getAttemptGrade(self):
        a = self.grade1.getAttemptGrade(1)
        self.assertEqual(2,a,msg="The grade for Attempt 1 is incorrect")
    
    def test_getAttemptGrade_out_of_range(self):
        try:
            self.grade2.getAttemptGrade(1)
        except IndexError:
            pass
        

    def test_check_answer(self):       
        self.grade1.check_answer()
        b=self.grade1.gradelist
        self.assertEqual(self.grade_dict.get("student1"),b,msg="the answer is checked incorrectly")

    def test_getStudent(self):
        a=self.grade1.getStudent()
        self.assertEqual("student1",a,msg="Get wrong student")

    def test_getNumAttempts(self):
        a=self.grade1.getNumAttempts()
        self.assertEqual(3,a,msg="The total number of attempts is incorrect")

if __name__ == '__main__':
    unittest.main()


