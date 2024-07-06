import tkinter as tk
from tkinter import messagebox
from lessons import create_lessons
from quiz import create_quizzes

class TeachMathApp:
    def __init__(self):
        self.lessons = create_lessons()
        self.quizzes = create_quizzes()
        self.current_lesson = None
        self.current_quiz = None

    def run(self):
        self.root = tk.Tk()
        self.root.title("TeachMath")

        self.label = tk.Label(self.root, text="Welcome to TeachMath!")
        self.label.pack()

        self.lesson_listbox = tk.Listbox(self.root)
        for lesson in self.lessons:
            self.lesson_listbox.insert(tk.END, lesson.title)
        self.lesson_listbox.pack()

        self.start_lesson_button = tk.Button(self.root, text="Start Lesson", command=self.start_lesson)
        self.start_lesson_button.pack()

        self.quiz_button = tk.Button(self.root, text="Take Quiz", command=self.start_quiz)
        self.quiz_button.pack()

        self.root.mainloop()

    def start_lesson(self):
        selected_index = self.lesson_listbox.curselection()
        if selected_index:
            self.current_lesson = self.lessons[selected_index[0]]
            messagebox.showinfo("Lesson Info", f"Lesson: {self.current_lesson.title}\nContent: {self.current_lesson.content}")

    def start_quiz(self):
        if self.quizzes:
            self.current_quiz = self.quizzes.pop(0)
            answer = tk.simpledialog.askstring("Quiz", self.current_quiz.question)
            if self.current_quiz.check_answer(answer):
                messagebox.showinfo("Quiz Result", "Correct!")
            else:
                messagebox.showinfo("Quiz Result", f"Incorrect! The correct answer is {self.current_quiz.answer}")
        else:
            messagebox.showinfo("Quiz", "No more quizzes available.")
