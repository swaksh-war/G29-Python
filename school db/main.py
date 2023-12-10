from Scorecard import Score, ScoreCard
from Teacher import Teacher, TeacherTable
from Student import Student, StudentTable
from Staff import Staff, StaffTable
from DummyData import *

class SchoolDB:
    def __init__(self, teacher_list:TeacherTable, student_list:StudentTable, staff_list:StaffTable):
        self.db = {
            'Teacher' : teacher_list,
            'Student' : student_list,
            'Staff' : staff_list
        }
    
    def show_db(self):
        for type_, table in self.db.items():
            print(type_)
            print(table)
    
    def add_new_student(self, student_obj : Student):
        self.db['Student'].add_student_data(student_obj)
        return student_obj
    

    def add_new_teacher(self, teacher_obj : Teacher):
        self.db['Teacher'].add_teacher_data(teacher_obj)
        return teacher_obj

    def add_new_staff(self, staff_obj : Staff):
        self.db['Staff'].add_staff_data(staff_obj)
        return staff_obj

if __name__ == '__main__':
    tTable = TeacherTable()
    tTable.add_teacher_data(madhu_teacher)

    stuTable = StudentTable()
    stuTable.add_student_data(balaji_student)

    staTable = StaffTable()
    staTable.add_staff_data(shaik_staff)

    g29db = SchoolDB(tTable, stuTable, staTable)
    g29db.show_db()
    print('\n\n\n')
    g29db.add_new_student(narendhra_student)
    g29db.add_new_teacher(jayasree_teacher)
    g29db.add_new_staff(bhanu_staff)
    g29db.show_db()
