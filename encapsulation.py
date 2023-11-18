'''encapsulation in python '''
class student:
    # constructor
    def __init__(self, name, rollno,subject ):
        # data members
        self.name = name
        self.rollno = rollno
        self.subject = subject

    # method
    # to display student's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'rollno:', self.rollno)

    # method
    def work(self):
        print(self.name, 'is studing in', self.subject)

# creating object of a class
st = student('ritu', 2004651, 'cse')

# calling public method of the class
st.show()
st.work()