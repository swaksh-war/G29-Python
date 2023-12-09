class Staff:
    def __init__(self, name : str, department : str):
        self.name = name
        self.department = department
    def __str__(self):
        return self.name

class StaffTable:
    def __init__(self):
        self.staff_table = []
    
    def __str__(self):
        return f"Table contains data of {len(self.staff_table)} staffs."
    
    def add_staff_data(self, staff_data : Staff):
        self.staff_table.append(staff_data)
        return staff_data

    def get_staff_data(self, id : int):
        return self.staff_table[id-1]
    
    def update_staff_data(self, id : int, **kwargs):
        staff_ins = self.staff_table[id-1]
        for key, val in kwargs.items():
            if key == 'name':
                staff_ins.name = val
            elif key == 'department':
                staff_ins.department = val
    
    def delete_staff_data(self, id : int):
        self.staff_table[id-1] = None
    
    def list_of_staff(self):
        for staff in self.staff_table:
            if staff is not None:
                print(staff)
