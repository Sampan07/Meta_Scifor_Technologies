import tkinter as tk
from tkinter import ttk


def submit_form():
    # Retrieve form data
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    address = text_address.get("1.0", tk.END)
    email = entry_email.get()
    contact_no = entry_contact.get()
    country = entry_country.get()
    state = entry_state.get()
    symptoms = []
    if var_cold.get():
        symptoms.append("Cold")
    if var_cough.get():
        symptoms.append("Cough")
    if var_fever.get():
        symptoms.append("Fever")
    if var_headache.get():
        symptoms.append("Headache")

    # Print form data (for demonstration purposes)
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact_no)
    print("Country:", country)
    print("State:", state)
    print("Symptoms:", symptoms)


# Create main window
root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Create and place labels and entries
tk.Label(root, text="Name of the visitor").grid(row=0, column=0, sticky=tk.W)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age of the visitor").grid(row=1, column=0, sticky=tk.W)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)
tk.Label(root, text="Gender").grid(row=2, column=0, sticky=tk.W)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky=tk.W)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky=tk.W)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").grid(row=2, column=3, sticky=tk.W)
tk.Label(root, text="Address").grid(row=3, column=0, sticky=tk.W)
text_address = tk.Text(root, height=4, width=30)
text_address.grid(row=3, column=1, columnspan=3)

tk.Label(root, text="Email Id").grid(row=4, column=0, sticky=tk.W)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1)

tk.Label(root, text="Contact No").grid(row=5, column=0, sticky=tk.W)
entry_contact = tk.Entry(root)
entry_contact.grid(row=5, column=1)

tk.Label(root, text="Country").grid(row=6, column=0, sticky=tk.W)
entry_country = tk.Entry(root)
entry_country.grid(row=6, column=1)

tk.Label(root, text="State").grid(row=7, column=0, sticky=tk.W)
entry_state = tk.Entry(root)
entry_state.grid(row=7, column=1)

tk.Label(root, text="Select if you have any of the following diseases").grid(row=8, column=0, columnspan=2, sticky=tk.W)
var_cold = tk.BooleanVar()
tk.Checkbutton(root, text="Cold", variable=var_cold).grid(row=9, column=0, sticky=tk.W)
var_cough = tk.BooleanVar()
tk.Checkbutton(root, text="Cough", variable=var_cough).grid(row=9, column=1, sticky=tk.W)
var_fever = tk.BooleanVar()
tk.Checkbutton(root, text="Fever", variable=var_fever).grid(row=9, column=2, sticky=tk.W)
var_headache = tk.BooleanVar()
tk.Checkbutton(root, text="Headache", variable=var_headache).grid(row=9, column=3, sticky=tk.W)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=10, column=0, columnspan=4)

# Start the main loop
root.mainloop()

