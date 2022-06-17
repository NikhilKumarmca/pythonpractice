from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("Its running")

# class Whiteboard(Computer):
#     def write(self):
#         print("its writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

com = Laptop()
pro = Programmer()

# com1 = Whiteboard()
pro.work(com)