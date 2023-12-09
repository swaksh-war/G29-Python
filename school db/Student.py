from Teacher import Teacher
from Scorecard import ScoreCard
class Student:
    def __init__(self, name : str, classnow : int, classTeacher : Teacher, ScoreCard : ScoreCard):
        self.name = name
        self.classNow = classnow
        self.classTeacher = classTeacher
        self.ScoreCard = ScoreCard
    