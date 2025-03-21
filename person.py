class Person:
    def __init__(self, name, age, address, ssn):
        self.name = name
        self.age = age
        self.address = address
        self.__ssn = ssn

    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, value):
        self.__ssn = value

    def role_duties(self):
        return "General responsibilities in the school system."

    def get_role(self):
        return "Person"
