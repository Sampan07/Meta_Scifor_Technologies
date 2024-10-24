import tkinter as tk
from math import sin, cos, tan, log, sqrt

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.configure(background='green')
        self.expression = ""

        self.input_text = tk.StringVar()

        # Create input field
        input_frame = tk.Frame(self.root, bd=10, bg='green')
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=20, insertwidth=4, width=14, bg='white')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Create button frame
        btns_frame = tk.Frame(self.root, bg='green')
        btns_frame.pack()

        # First row
        clear = tk.Button(btns_frame, text='AC', fg='black', bg='red', width=10, height=3, command=lambda: self.clear()).grid(row=0, column=0)
        add = tk.Button(btns_frame, text='+', fg='black', bg='red', width=10, height=3, command=lambda: self.click('+')).grid(row=0, column=1)
        subtract = tk.Button(btns_frame, text='-', fg='black', bg='red', width=10, height=3, command=lambda: self.click('-')).grid(row=0, column=2)
        multiply = tk.Button(btns_frame, text='*', fg='black', bg='red', width=10, height=3, command=lambda: self.click('*')).grid(row=0, column=3)

        # Second row
        cos_button = tk.Button(btns_frame, text='cos', fg='black', bg='red', width=10, height=3, command=lambda: self.click('cos')).grid(row=1, column=0)
        sin_button = tk.Button(btns_frame, text='sin', fg='black', bg='red', width=10, height=3, command=lambda: self.click('sin')).grid(row=1, column=1)
        tan_button = tk.Button(btns_frame, text='tan', fg='black', bg='red', width=10, height=3, command=lambda: self.click('tan')).grid(row=1, column=2)
        log_button = tk.Button(btns_frame, text='log', fg='black', bg='red', width=10, height=3, command=lambda: self.click('log')).grid(row=1, column=3)

        # Third row
        seven = tk.Button(btns_frame, text='7', fg='black', bg='red', width=10, height=3, command=lambda: self.click('7')).grid(row=2, column=0)
        eight = tk.Button(btns_frame, text='8', fg='black', bg='red', width=10, height=3, command=lambda: self.click('8')).grid(row=2, column=1)
        nine = tk.Button(btns_frame, text='9', fg='black', bg='red', width=10, height=3, command=lambda: self.click('9')).grid(row=2, column=2)
        divide = tk.Button(btns_frame, text='/', fg='black', bg='red', width=10, height=3, command=lambda: self.click('/')).grid(row=2, column=3)

        # Fourth row
        four = tk.Button(btns_frame, text='4', fg='black', bg='red', width=10, height=3, command=lambda: self.click('4')).grid(row=3, column=0)
        five = tk.Button(btns_frame, text='5', fg='black', bg='red', width=10, height=3, command=lambda: self.click('5')).grid(row=3, column=1)
        six = tk.Button(btns_frame, text='6', fg='black', bg='red', width=10, height=3, command=lambda: self.click('6')).grid(row=3, column=2)
        square = tk.Button(btns_frame, text='x2', fg='black', bg='red', width=10, height=3, command=lambda: self.click('**2')).grid(row=3, column=3)

        # Fifth row
        one = tk.Button(btns_frame, text='1', fg='black', bg='red', width=10, height=3, command=lambda: self.click('1')).grid(row=4, column=0)
        two = tk.Button(btns_frame, text='2', fg='black', bg='red', width=10, height=3, command=lambda: self.click('2')).grid(row=4, column=1)
        three = tk.Button(btns_frame, text='3', fg='black', bg='red', width=10, height=3, command=lambda: self.click('3')).grid(row=4, column=2)
        cube = tk.Button(btns_frame, text='x3', fg='black', bg='red', width=10, height=3, command=lambda: self.click('**3')).grid(row=4, column=3)

        # Sixth row
        mod = tk.Button(btns_frame, text='%', fg='black', bg='red', width=10, height=3, command=lambda: self.click('%')).grid(row=5, column=0)
        zero = tk.Button(btns_frame, text='0', fg='black', bg='red', width=10, height=3, command=lambda: self.click('0')).grid(row=5, column=1)
        dot = tk.Button(btns_frame, text='.', fg='black', bg='red', width=10, height=3, command=lambda: self.click('.')).grid(row=5, column=2)
        equals = tk.Button(btns_frame, text='=', fg='black', bg='red', width=10, height=3, command=lambda: self.equals()).grid(row=5, column=3)

    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equals(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
