class Pycharm:
    def execution(self):
        print("compiling")

class CustomEditor:
    def execution(self):
        print("compiling")
        print("dark Bg")
        print("spell check")

class Laptop:
    def code(self,ide):
        ide.execution()

ide = CustomEditor()
lap = Laptop()
lap.code(ide)