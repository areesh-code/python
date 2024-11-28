class parrot:
    species="Bird"
    def __init__(self, name, colour, age):
        self.name=name
        self.colour=colour
        self.age=age
Blu=parrot("Blu", "Green", 13)
Woot=parrot("Woot", "Orange", 8)
print("Blu is a {}" .format(Blu.species))
print("Woot is a {}" .format (Woot.species))
print("{} is {} years old {} in colour" .format(Blu.name, Blu.age, Blu.colour))
print("{} is {} years old {} in colour" .format(Woot.name, Woot.age, Woot.colour))


    
        