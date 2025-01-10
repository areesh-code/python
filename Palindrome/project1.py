student_names = []


print("Enter the names of 10 students:")
for i in range(10):
    name = input(f"Enter name of student {i+1}: ")
    student_names.append(name)


if len(student_names) > 1:
    removed_student = student_names.pop(1)
    print(f"\nRemoved the student at position 2: {removed_student}")


new_student = input("\nEnter the name of a new student to add at position 1: ")
student_names.insert(0, new_student)


print("\nFinal list of students:")
for idx, name in enumerate(student_names, start=1):
    print(f"{idx}: {name}")