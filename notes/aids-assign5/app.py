import os
import shelve
from flask import Flask, request, render_template
from assignment5 import *
from persistence import Persistence

app = Flask(__name__)

quiz = Quiz('Quiz 1', 4)
question1 = Question('question1', 5)
questionBank = QuestionBank()
questionBank.questions.append(question1)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz_list():
    return render_template('quiz.html')
    

@app.route('/quiz/question1')
def question_list():
    return render_template('question1.html')


    