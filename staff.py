from person import Person

class Staff(Person):
    def __init__(self, name, age, address, ssn, years_of_service, base_salary):
        super().__init__(name, age, address, ssn)
        self.years_of_service = years_of_service
        self.base_salary = base_salary
        self.salary = 0

    def calculate_salary(self):
        self.salary = self.base_salary + (self.base_salary * 0.05 * self.years_of_service)

    def get_salary(self):
        return self.salary

    def role_duties(self):
        return "Manage logistics, administrative tasks, and support school operations."

    def get_role(self):
        return "Staff"
