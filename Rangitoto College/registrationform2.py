import tkinter as tk
from tkinter import messagebox

# Data for male and female students
male_students = [{"name": "Jack"}, {"name": "Areesh"}]
female_students = [{"name": "Olivia"}, {"name": "Grace"}]

# Function to display the list of students in the text box
def display_students(students, list_widget):
    # Clear current list
    list_widget.delete(1.0, tk.END)
    # Add each student name to the list box
    for student in students:
        list_widget.insert(tk.END, student["name"] + "\n")

# Function to add a student to the list
def add_student(students, entry, list_widget):
    # Get the name from the entry box
    name = entry.get()
    if name:
        # Add the new student to the list
        students.append({"name": name})
        # Update the display
        display_students(students, list_widget)
        # Clear the entry box
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a name.")

# Function to delete a student from the list
def del_student(students, entry, list_widget):
    name = entry.get().lower()  # Convert name to lowercase for case-insensitive comparison
    for student in students:
        if student["name"].lower() == name:
            students.remove(student)  # Remove the student
            display_students(students, list_widget)  # Update the display
            entry.delete(0, tk.END)  # Clear the entry box
            return
    messagebox.showwarning("Student Not Found", f"Student {name} not found.")  # Show warning if not found

# Create the main window
root = tk.Tk()
root.title("Rangitoto College")

# Create a frame for male students
male_frame = tk.Frame(root)
male_frame.pack(pady=10)
tk.Label(male_frame, text="Male Students").grid(row=0, column=0)
male_list = tk.Text(male_frame, height=10, width=30)  # Text box to display male students
male_list.grid(row=1, column=0)
male_entry = tk.Entry(male_frame)  # Entry box for entering male student names
male_entry.grid(row=2, column=0)
# Buttons for adding and deleting male students
tk.Button(male_frame, text="Add Male Student", command=lambda: add_student(male_students, male_entry, male_list)).grid(row=3, column=0)
tk.Button(male_frame, text="Delete Male Student", command=lambda: del_student(male_students, male_entry, male_list)).grid(row=4, column=0)

# Create a frame for female students
female_frame = tk.Frame(root)
female_frame.pack(pady=10)
tk.Label(female_frame, text="Female Students").grid(row=0, column=0)
female_list = tk.Text(female_frame, height=10, width=30)  # Text box to display female students
female_list.grid(row=1, column=0)
female_entry = tk.Entry(female_frame)  # Entry box for entering female student names
female_entry.grid(row=2, column=0)
# Buttons for adding and deleting female students
tk.Button(female_frame, text="Add Female Student", command=lambda: add_student(female_students, female_entry, female_list)).grid(row=3, column=0)
tk.Button(female_frame, text="Delete Female Student", command=lambda: del_student(female_students, female_entry, female_list)).grid(row=4, column=0)

# Display the initial list of students
display_students(male_students, male_list)
display_students(female_students, female_list)

# Button to exit the application
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

# Run the Tkinter event loop to show the window
root.mainloop()



