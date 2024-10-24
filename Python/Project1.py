'''In a coding class the teacher has taught the kids about the python GUI and has now assigned the following task to the students

1) Create a random name picker from a given list of students

2) should have a button clicking on which a random name should be picked

3) Once the random name is picked the name should be removed from the list so that the name is not repeated and also the removed name should show in completed section
#create a GUI with two sections one to see the randomly generated name and the other one to see the names that are generated randomly and which are not suppose to be considered for generating randomly again.'''
import random
import tkinter as tk
students = ["Steve","Rogers","Alice","Bruce","Samuel"]
window = tk.Tk()
window.title("Random Name Generator")
completed_names = []
def pick_name():
    if not students:
        pick_name_label.config(text="All names completed",fg="red")
        return
    picked_name=random.choice(students)
    pick_name_label.config(text=f"Name Picked: {picked_name}",fg="green")
    students.remove(picked_name)
    completed_names.append(picked_name)
    completed_names_label = tk.Label(completed_names_frame,text=picked_name,fg="lightgreen",bg="grey")
    completed_names_label.pack()

pick_name_label = tk.Label(window,text="Click below to pick a name randomly")
pick_name_label.pack(pady=20)

pick_name_button = tk.Button(window,text="Click Here",command=pick_name)
pick_name_button.pack(pady=15)

completed_names_label = tk.Label(window,text="Completed Names",fg="black")
completed_names_label.pack(pady=10)
completed_names_frame = tk.Frame(window)
completed_names_frame.pack(pady=10)




window.mainloop()