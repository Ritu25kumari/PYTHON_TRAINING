from abc import ABC,  abstractmethod
class Animal(ABC):
      @abstractmethod
      def eat1(self):
         pass
      @abstractmethod
      def eat2(self):
         pass
class Dog(Animal):
         def eat1(self):
            print("dog implementation..")

class cat(Dog):
         def eat2(self):
            print("cat impemantation..")
c=Dog()
c.eat1()
c.eat2()