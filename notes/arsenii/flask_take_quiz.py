from flask import Flask, render_template, request
from stub_quiz import Quiz, Question, MultipleChoice
from take_quiz import QuizInProgress
app = Flask(__name__)

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
qp.loadQuiz(q)

@app.route('/')
def quiz():
    
    return render_template('main.html', result=qp.getQuestions())


@app.route('/quiz', methods=['POST'])
def quiz_sub():
    return '<h1>Submitted</u></h1>'

@app.route('/pause', methods=['POST'])
def quiz_paus():
    return '<h1>Quiz on Pause</u></h1>'


if __name__ == '__main__':
    app.run(debug=True)
