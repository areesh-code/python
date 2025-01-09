import random

college_name = "Rangitoto College"


male_students = [
    {"name": "Jack"},
    {"name": "Areesh"},
]

def display_male_students():
    print(f"Students at {college_name} - Male Students")
    for student in male_students:
        print(f"Name: {student['name']}")

def add_male_student():
    name = input("Enter student's name: ")
    male_students.append({"name": name})
    print(f"Student {name} added successfully!")

def del_male_student():
    name = input("Enter student's name to delete: ")
    for student in male_students:
        if student["name"].lower() == name.lower():
            male_students.remove(student)
            print(f"Student {name} deleted successfully!")
            return
    print(f"Student {name} not found.")

def male_student_menu():
    while True:
        print("\n--- Male Student Menu ---")
        print("1. Display all male students")
        print("2. Add a male student")
        print("3. Delete a male student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_male_students()
        elif choice == '2':
            add_male_student()
        elif choice == '3':
            del_male_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


female_students = [
    {"name": "Olivia"},
    {"name": "Grace"},
]

def display_female_students():
    print(f"Students at {college_name} - Female Students")
    for student in female_students:
        print(f"Name: {student['name']}")

def add_female_student():
    name = input("Enter student's name: ")
    female_students.append({"name": name})
    print(f"Student {name} added successfully!")

def del_female_student():
    name = input("Enter student's name to delete: ")
    for student in female_students:
        if student["name"].lower() == name.lower():
            female_students.remove(student)
            print(f"Student {name} deleted successfully!")
            return
    print(f"Student {name} not found.")

def female_student_menu():
    while True:
        print("\n--- Female Student Menu ---")
        print("1. Display all female students")
        print("2. Add a female student")
        print("3. Delete a female student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_female_students()
        elif choice == '2':
            add_female_student()
        elif choice == '3':
            del_female_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Male Student Menu")
        print("2. Female Student Menu")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            male_student_menu()
        elif choice == '2':
            female_student_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()