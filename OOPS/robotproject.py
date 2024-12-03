class Robot:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def introduce(self):
        print(f"Hello, I am {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My hobby is {self.hobby}.\n")
    
tom = Robot("Tom", 13, "Cricket") 
jerry = Robot("Jerry", 10, "Basketball")

tom.introduce()
jerry.introduce()