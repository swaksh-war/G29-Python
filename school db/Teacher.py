class Teacher:
    def __init__(self, name : str, subject : str):
        self.name = name
        self.subject = subject
    def __str__(self):
        return self.name

class TeacherTable:
    def __init__(self):
        self.teacher_table = []

    def __str__(self):
        return f"Table contains data of {len(self.teacher_table)} teachers."

    def add_teacher_data(self, teacher_data : Teacher):
        self.teacher_table.append(teacher_data)
        return teacher_data

    def get_teacher_data(self, id : int):
        return self.teacher_table[id-1]

    def update_teacher_data(self, id : int, **kwargs):
        teacher_ins = self.teacher_table[id-1]
        for key, val in kwargs.items():
            if key == 'name':
                teacher_ins.name = val
            elif key == 'subject':
                teacher_ins.subject = val

    def delete_teacher_data(self, id : int):
        self.teacher_table[id-1] = None

    def list_of_teacher(self):
        for teacher in self.teacher_table:
            if teacher is not None:
                print(teacher)

if __name__ == '__main__':
    t1 = Teacher(name='Swakshwar', subject='Python-ML-DL')
    teacherDB = TeacherTable()
    teacherDB.add_teacher_data(t1)
    print(teacherDB)
    print(t1)