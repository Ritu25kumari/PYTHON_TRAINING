class Student:
    schoolName = 'XYZ School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute
        def show(self):
            print("Name: ", self.name, 'age:', self.age)
s = Student('ritu kumari', 20)
s.show()