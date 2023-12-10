from Teacher import Teacher
from Scorecard import ScoreCard
class Student:
    def __init__(self, name : str, classnow : int, classTeacher : Teacher, ScoreCard : ScoreCard):
        self.name = name
        self.classNow = classnow
        self.classTeacher = classTeacher
        self.ScoreCard = ScoreCard

class StudentTable:
    def __init__(self):
        self.student_table = []
    
    def __str__(self):
        return f"Table contains data of {len(self.student_table)} students."
    
    def add_student_data(self, student_data : Student):
        self.student_table.append(student_data)
        return student_data

    def get_student_data(self, id : int):
        return self.student_table[id-1]
    
    def update_student_data(self, id : int, **kwargs):
        student_ins = self.student_table[id-1]
        for key, val in kwargs.items():
            if key == 'name':
                student_ins.name = val
            elif key == 'classnow':
                student_ins.department = val
    
    def delete_student_data(self, id : int):
        self.student_table[id-1] = None
    
    def list_of_student(self):
        for student in self.student_table:
            if student is not None:
                print(student)
