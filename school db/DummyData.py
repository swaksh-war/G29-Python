from Teacher import Teacher
from Student import Student
from Scorecard import ScoreCard, Score
from Staff import Staff

madhu_teacher = Teacher(name='madhu', subject='python')
jayasree_teacher = Teacher(name='Jayasree', subject='maths')

# Creating BALAJI Data
balaji_python_score = Score(subject='python', score = 92)
balaji_maths_score = Score(subject='maths', score =88)
balaji_score_card = ScoreCard([balaji_python_score, balaji_maths_score])
balaji_student = Student(name='balaji', classnow=10, classTeacher=madhu_teacher, ScoreCard = balaji_score_card)

# Creating Narendhra Data
narendhra_python_score = Score(subject='python', score = 93)
narendhra_maths_score = Score(subject='math', score=85)
narendhra_score_card = ScoreCard([narendhra_python_score, narendhra_maths_score])
narendhra_student = Student(name='narendhra', classnow=10, classTeacher=jayasree_teacher, ScoreCard=narendhra_score_card)

# Staff Shaik
shaik_staff = Staff(name='Shaik', department='Administrative')
# Bhanu Staff
bhanu_staff = Staff(name='Bhanu', department='Examination')

