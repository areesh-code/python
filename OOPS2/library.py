class Library:
    def __init__(self,name,list):
        self.name= name
        self.list= list
        self.dic= {}
    def display(self):
        print("Welcome to the", self.name, "library") 
        for i in self.list:
            print(i)
    def add_book(self,book):
        self.list.append(book)
        print("Your book has now added")
    def lenbook(self,book,user):
        if book not in self.dic.keys():
            self.dic.update({book:user})
            print("You can now finally take this book")
        else:
            print("It is already sadly been taken")
obj= Library("Areesh Library", ["Harry poter", "Diary of the Wimpy Kid", "Wonder", "BFG"])
while True:
    print("Press 1 for display, press 2 to add book, press 3 to lend book")
    x= int(input())
    if x==1:
        obj.display()
    elif x==2:
        name=input("Enter the name of the book")
        obj.add_book(name)
    elif x==3:
        name = input("Enter the name of the user")
        bookname = input("Enter the name of the book")
        obj.lenbook(bookname,name)
    
    


    
    
        
    