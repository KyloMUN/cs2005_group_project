Public Data Structures

- Question:
 fields:
  - id: shortid
  - display: string
  - answers: dict<key>(display: string)
  - choices: dict<key>(display: string)
  - points: int

- Quiz
 Fields:
  - id: shortid
  - name: string
  - questions: List<Question>
  - num\_of\_attempts: int
  - start\_time: datetime
  - end\_time: datetime
  - time\_limit: datetime

- Person
 fields:
  - id: shortid

- Class 
 fields:
  - id: shortid
  - quizes: List<QuizesInProgress>

Private Data Structures:

QuizSession
 fields:
  - id: shortid
  - submitted: boolean

QuestionWithData(Question):
 fields:
  - picked: [key]

