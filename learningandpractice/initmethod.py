class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ",self.cpu,self.ram)

com1 = Computer("i5","12GB")
com2 = Computer("ryzon1200","12GB")

com1.config()
com2.config()