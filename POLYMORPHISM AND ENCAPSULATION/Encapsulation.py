class Computer:
    def __init__(self):
        self.__Price= 679
    def display(self):
        print(self.__Price)

    def Change(self, Newprice):
        self.__Price= Newprice

obj1 = Computer()
obj1.display()

obj1.__Price= 740
obj1.display()
obj1.Change(740)
obj1.display()