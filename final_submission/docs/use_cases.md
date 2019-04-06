# Use Cases

## Login, Authenticate, Persistence

Title: Creating and logging into the application

Primary Actor: Professor

Stakeholders and Interests:

- Student: Wants an account to view quizzes for a class he is physically enrolled in.

- Professor: Wants to create account for student, and assign to class.

Tech: Does not want to have the password for any of the above stakeholders to be stored in the database/logs, but wants all created users to end up stored in the database correctly.

Precondition: Professors account exists in the storage.

Main Scenario:

1. Professor logs into account with correct credentials

> 1. If credentials are incorrect, is not logged in.

1. Professor navigates to page to create a new user.

1. Professor creates a new user.

> 1. Professor is not permitted to create a user with the username of a user already in storage.

1. Professor adds new user to a class.

1. Student logs in.

> 1. If credentials are incorrect, is not logged in.

1. Student can view quizzes for class he was assigned to by the Professor.

## Create Quiz

Title: Create Quiz

Primary Actor: Instructor

Stakeholders:

- Student: Wants to take quiz.

- Instructor: Wants to make quiz.

- Technician: Wants a smooth running system.

Precondition: User is logged in as a instructor.

Main Scenario:

1. Instructor navigates to create quiz interface using a button on their home page.

> 1. Instructor can also follow a direct link.

2. Instructor is presented a form to begin building their quiz. 

> 1. Quiz saved for later time to finish, if undone at release time, is not deployed.

1. Instructor fills out all fields in their form and reaches point where they need only to add questions.

> 1. Unfilled attributes
>
> 1. Unfinished quiz can be opened to be finished.

1. Instructor adds a question, is presented with the option to add a new one. Form extends if they do.

> 1. Not priority, deploying with 3 questions for functionality.

1. Quiz is saved by professor when they are satisfied.

> 1. Can be changed before start date.

1. Questions in the quiz are sent to the question bank.

> 1. Question Bank can be accessed at any time

1. Quiz is passed to storage.

> 1. Instructor cannot modify the quiz after start time.

## Take Quiz

Title: Take Quiz

Primary Actor: Student

Stakeholders and Interests:

- Student: Wants to take a quiz.

Preconditions:

Student already logged in.

Quiz created.

Main scenario:

1. User opens quiz.

> 1. User has exhausted attempts, is shown a message they may not proceed with the quiz and they can go to the main menu or log out.

1. User chooses answers for questions.

1. User submits quiz.

1. User is moved to page of submission.

1. User may now go to main menu or log out.

## Automatic Grading

Title: Review Class Result

Primary Actor: Instructor

Stakeholders and Interests:

- Instructor: Wants to review the class result of a quiz

- Precondition: User with Instructor privileges logged in already.

Main Scenario:

1. Instructor selects quiz for review

1. SuD lists class result and student submissions

1. Instructor selects class result

1. SuD displays the quiz items from top to bottom follows the order: participation, then average grade, then the histogram.

1. Instructor return to the previous page and select student submissions

1. SuD list all the student name with corresponding id that can take the quiz

1. Instructor select one of the student as desired

1. SuD displays items from to bottom follows the order: the student name, id, then the attempt 1 with its grade, then attempt 2 with its grade up to the number of attempts that the student took, lastly the highest grade

> 1. No attempts shows if student did not take the quiz

> 1. Instructor select one of the attempt as desired.

1. SuD displays the quiz questions with its corresponding correct answers and also with the student answers for instructor to review

> 1. Any question without a student answer means the student did not answer the corresponding question

1. Instructor repeats step 9 to 10.

1. Instructor repeats step 5 to 11.

### Manual Grading

Title: Correct a True or False Question

Primary Actor: Instructor

Stakeholders and Interests:

- Instructor: Wants to fix an answer to a question.

- Student: Wants a higher grade on the question.

- Other Instructors: Wants a note of the change made.

Precondition: Instructor is logged into the persistence system in their instructor account.

Main Scenario:

1. Instructor pulls quiz from system, with it’s grading and question set included.

1. Instructor chooses the question of interest and runs a program over it to change the correct answer.

1. The instructor logs this change for later review.

1. The system receives the correct answer, goes back through the persistence and correctly modifies the automatic grading components with no input from instructor.

1. Instructor repeats 2-4 for however many broken questions there may be.

1. Instructor logs out. 

