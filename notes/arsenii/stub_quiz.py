import datetime
class Quiz:
    def __init__(self, numofattempts, starttime=None, endtime=datetime.datetime.now(), timelimit=None):
        self._questions = []
        self._numofattempts = numofattempts
        self._starttime = starttime
        self._endtime = endtime
        self._timelimit = timelimit
        self._questionnumber = len(self._questions)

    def get_num_of_attempts(self):
       
        return self._numofattempts

    def addQuest(self, quest):
        self._questions.append(quest)

    def get_time_limit(self):
       
        return self._timelimit

    def get_question_set(self):
        return self._questions

    def is_available(self):
        if datetime.datetime.now() >= self._endtime:
            return True
        else:
            return False

class Question:
     def __init__(self, questiontext, correctanswer, displaytext=None):
        self._question_id = 0
        self._questiontext = questiontext
        self._answers = []
    
     def get_question_id(self):
        
        return self._question_id
    
     def set_quest_id(self, newid):
         self._question_id = newid

     
        
class MultipleChoice(Question):
    

    def __init__ (self, questiontext, correctanswer,  listofoptions):
        super().__init__(questiontext, correctanswer)
        self._listofoptions = listofoptions

    def add_option(self, newoption):

        self._listofoptions.append(newoption)
    def getQuestionText(self):
        return self._questiontext
    def getOptions(self):
        return self._listofoptions

if __name__ == "__main__":     
    q= Quiz(3)


    c1 = MultipleChoice("question1", "one", ["one", "two", "three", "four"])
    c2 = MultipleChoice("question2", "two",["one", "two", "three", "four"])
    c3 = MultipleChoice("question3", "three", ["one", "two", "three", "four"])
    c4 = MultipleChoice("question4", "four", ["one", "two", "three", "four"])
    c1.set_quest_id(1)
    c2.set_quest_id(2)
    c3.set_quest_id(3)
    c4.set_quest_id(4)
    mylist=[]
    mylist.append(c1)
    mylist.append(c2)
    mylist.append(c3)
    mylist.append(c4)
    for i in mylist:
        q.addQuest(i)
    for i in q.get_question_set():
        print(i.getQuestionText())
        print(i.getOptions())
    print(c1.get_question_id())
    print(c1.getQuestionText())
    print(c1.getOptions())
    print(q.get_num_of_attempts())
    print(q.is_available())
    print(datetime.datetime.now())

