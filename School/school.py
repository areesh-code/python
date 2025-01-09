import random

school_name = "Murrays Bay Intermediate"

male_students = [
    {"name": "Jack", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Cade", "grade": 8, "age": 12, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Mathew", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Freddie", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Julian", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Jackson", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Cooper", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Yibo", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "John", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Luke", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Eli", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Male"},
    {"name": "Areesh", "grade": 8, "age": 13, "classroom": 24, "gender": "Male"}
]

def display_male_students():
    print(f"Students at {school_name} - Male Students")
    for student in male_students:
        print(f"Name: {student['name']}, Grade: {student['grade']}, Age: {student['age']}, "
              f"Classroom: {student['classroom']}, Gender: [✓ Male]")

def add_male_student():
    name = input("Enter the student's name: ")
    grade = int(input("Enter the student's grade (7 or 8): "))
    age = int(input("Enter the student's age (12 or 13): "))
    classroom = random.randint(1, 45)
    male_students.append({"name": name, "grade": grade, "age": age, "classroom": classroom, "gender": "Male"})
    print(f"Student {name} added successfully!")


def delete_male_student():
    name = input("Enter the name of the student to delete: ")
    for student in male_students:
        if student['name'].lower() == name.lower():
            male_students.remove(student)
            print(f"Student {name} deleted successfully!")
            return
    print("Student not found.")


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
            delete_male_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


male_student_menu()

import random


female_students = [
    {"name": "Olivia", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Emma", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Ava", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Sophia", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Isabella", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Mia", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Amelia", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Harper", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Ella", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    {"name": "Grace", "grade": 8, "age": 13, "classroom": random.randint(1, 45), "gender": "Female"},
    
]

def display_female_students():
    print(f"Students at {school_name} - Female Students")
    for student in female_students:
        print(f"Name: {student['name']}, Grade: {student['grade']}, Age: {student['age']}, "
              f"Classroom: {student['classroom']}, Gender: [✓ Female]")


def add_female_student():
    name = input("Enter the student's name: ")
    grade = int(input("Enter the student's grade (7 or 8): "))
    age = int(input("Enter the student's age (12 or 13): "))
    classroom = random.randint(1, 45)
    female_students.append({"name": name, "grade": grade, "age": age, "classroom": classroom, "gender": "Female"})
    print(f"Student {name} added successfully!")

def delete_female_student():
    name = input("Enter the name of the student to delete: ")
    for student in female_students:
        if student['name'].lower() == name.lower():
            female_students.remove(student)
            print(f"Student {name} deleted successfully!")
            return
    print("Student not found.")

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
            delete_female_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


female_student_menu()



