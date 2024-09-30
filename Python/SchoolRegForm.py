import tkinter as tk
from tkinter import messagebox
def register():
    name=enter_name.get()
    age=enter_age.get()
    fname=enter_fname.get()
    address = enter_address.get()
    contact=enter_cno.get()
    status=status_var.get()
    if not (name and age and fname and address and contact and status):
        messagebox.showerror("Please Enter all fields")
        return
    print(f"Name: {name}")
    print(f"Father's Name: {fname}")
    print(f"Age: {age}")
    print(f"Address: {address}")
    print(f"Contact Number: {contact}")
    print(f"Previous Grade Status: {status}")

    messagebox.showinfo("Registration Successful")

window = tk.Tk()
window.title("School Registration Form")

tk.Label(window,text="Enter your name").grid(row=0,column=0)
enter_name=tk.Entry(window)
enter_name.grid(row=0,column=1)

tk.Label(window,text="Enter your age").grid(row=1,column=0)
enter_age=tk.Entry(window)
enter_age.grid(row=1,column=1)

tk.Label(window,text="Enter your Father's Name").grid(row=2,column=0)
enter_fname=tk.Entry(window)
enter_fname.grid(row=2,column=1)

tk.Label(window,text="Enter your Address").grid(row=3,column=0)
enter_address=tk.Entry(window)
enter_address.grid(row=3,column=1)

tk.Label(window,text="Enter your Contact Number").grid(row=4,column=0)
enter_cno=tk.Entry(window)
enter_cno.grid(row=4,column=1)

tk.Label(window,text="Previous Grade status").grid(row=5,column=0)
status_var = tk.StringVar(value="")

btn_passed = tk.Radiobutton(window,text="Passed",variable=status_var,value="Passed")
btn_failed = tk.Radiobutton(window,text="Failed",variable=status_var,value="Failed")
btn_passed.grid(row=5,column=1,sticky="w",padx=10)
btn_failed.grid(row=6,column=1,sticky="w",padx=10)

btn_register=tk.Button(window,text="Register",command=register)
btn_register.grid(row=7,columnspan=2,pady=20)

window.mainloop()