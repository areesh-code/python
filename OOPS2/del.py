class student:
    def __init__(self):
        print("Constructer is called")
    def __del__(self):
        print("Destuct is created")
obj= student()
del obj
print(obj)