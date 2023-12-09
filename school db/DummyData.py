from Teacher import Teacher
from Student import Student
from Scorecard import ScoreCard, Score

madhu_teacher = Teacher(name='madhu', subject='python')
jayasree_teacher = Teacher(name='Jayasree', subject='maths')

# Creating BALAJI Data
balaji_python_score = Score(subject='python', score = 92)
balaji_maths_score = Score(subject='maths', score =88)
balaji_score_card = ScoreCard([balaji_python_score, balaji_maths_score])
balaji_student = Student(name='balaji', classnow=10, classTeacher=madhu_teacher, ScoreCard = balaji_score_card)