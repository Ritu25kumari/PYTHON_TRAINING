# Example 4
class NegativeAgeException(RuntimeError):
     def _init_(self, age):
         super()._init_()
         self.age = age
def status(age):
         if age < 0:
             raise NegativeAgeException("Only positive integers are allowed")
         if age>22:
             print("Eligible for mrg")
         else:
             print("not Eligible for mrg....")
try:
     num = int(input("Enter your age: "))
     status(num)
except NegativeAgeException:
     print("Only positive integers are allowed")
except:
     print("something is wrong")

    #  output
    '''
    Enter your age: 20
not Eligible for mrg....
    '''

    