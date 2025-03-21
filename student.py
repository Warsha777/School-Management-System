from person import Person

class Student(Person):
    def __init__(self, name, age, address, ssn):
        super().__init__(name, age, address, ssn)
        self.grades = {}
        self.attendance_record = []
        self.average_grade = 0

    def assign_grades(self, grades_dict):
        self.grades = grades_dict
        total = sum(grades_dict.values())
        self.average_grade = total / len(grades_dict) if grades_dict else 0

    def attendance(self, status):
        self.attendance_record.append(status.lower() == "present")

    def role_duties(self):
        return "Attend classes, complete assignments, and take exams."

    def get_role(self):
        return "Student"

    def get_attendance_record(self):
        present = sum(self.attendance_record)
        total = len(self.attendance_record)
        return f"Attendance: {present}/{total}"
