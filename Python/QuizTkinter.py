import tkinter as tk
from tkinter import messagebox
import json


class QuizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.load_questions()
        self.score = 0
        self.question_index = 0
        self.selected_option = tk.StringVar()

        self.create_widgets()
        self.display_question()

    def load_questions(self):
        with open('questions.json', 'r') as file:
            self.questions = json.load(file)

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.options = []
        for _ in range(4):
            radio = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="")
            radio.pack(anchor="w")
            self.options.append(radio)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(side="left", padx=20, pady=20)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(side="right", padx=20, pady=20)

    def display_question(self):
        question_data = self.questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        self.selected_option.set("")
        for i, option in enumerate(question_data["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        if self.selected_option.get() == self.questions[self.question_index]["answer"]:
            self.score += 1

        self.question_index += 1

        if self.question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your score is {self.score}/{len(self.questions)}")
        self.root.quit()



window = tk.Tk()
app = QuizApp(window)
window.mainloop()