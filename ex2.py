# Example 2
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
     def _init_(self, value):
         self.value = value
         super()._init_()

     @abstractmethod
     def do_something(self):
         pass
 
class DoAdd(AbstractClassExample):
     def do_something(self):
      return self.value + 42
 
class DoMul(AbstractClassExample):
 
     def do_something(self):
         return self.value * 42
 
x = DoAdd(10)
y = DoMul(10)
print(x.do_something())
print(y.do_something())

# output
'''
52
420
'''