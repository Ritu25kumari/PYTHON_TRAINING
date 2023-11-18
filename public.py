class student:
    # constructor
    def __init__(self, name, branch):
        #  public data members
        self.name = name
        self.branch = branch
    def show(self):
        print("Name: ", self.name, 'branch:', self.branch)
s = student('ritu kumari', 'cse')
s.show()
