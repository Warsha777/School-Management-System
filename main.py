from student import Student
from teacher import Teacher
from staff import Staff

def main():
    student = Student("Alice", 15, "123 Main St", "111-22-3333")
    student.assign_grades({"Math": 92, "Science": 88, "History": 75})
    student.attendance("Present")
    student.attendance("Absent")
    
    teacher = Teacher("Mr. Smith", 40, "456 Oak Ave", "222-33-4444", "Mathematics", [])
    teacher.schedule_classes(["Math", "Algebra", "Geometry"])
    
    staff = Staff("Mrs. Johnson", 35, "789 Pine Rd", "333-44-5555", 5, 3000)
    staff.calculate_salary()
    
    people = [student, teacher, staff]
    for person in people:
        print(f"Name: {person.name}, Age: {person.age}, Role: {person.get_role()}")
        print(person.role_duties())
        if person.get_role() == "Student":
            print(student.get_attendance_record())
            print(f"Average Grade: {student.average_grade:.2f}")
        elif person.get_role() == "Staff":
            print(f"Calculated Salary: {staff.get_salary()}")
        print()

main()