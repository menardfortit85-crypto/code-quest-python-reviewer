import tkinter as tk
from tkinter import messagebox

# CODE QUEST - Python Learning Portal
# A beginner-friendly reviewer made with Tkinter.

BG = "#F4F7FB"
WHITE = "#FFFFFF"
NAVY = "#172B4D"
BLUE = "#3478F6"
LIGHT_BLUE = "#EAF1FF"
DARK = "#26364A"
GRAY = "#718096"
GREEN = "#27AE60"

root = tk.Tk()
root.title("Code Quest | Python Learning Portal")
root.geometry("1050x700")
root.minsize(900, 600)
root.configure(bg=BG)

registered_name = ""
registered_password = ""
completed = []
current_question = 0
score = 0
selected_answer = tk.StringVar()

lessons = [
    {
        "title": "Introduction to Computing",
        "description": "Understand how a computer receives and handles information.",
        "content": """Computing is the process of using a computer to work with information.

The four basic operations are:
• Input - data entered into the computer.
• Processing - the computer works on the data.
• Output - the result shown to the user.
• Storage - saving data for later use.

Example: When you type a message, the keyboard is input, the computer processes it, the screen displays output, and saving the message is storage."""
    },
    {
        "title": "Python Basic Syntax",
        "description": "Learn the basic rules for writing Python instructions.",
        "content": """Syntax refers to the rules used to write a program. Python uses indentation (spaces at the beginning of a line) to group instructions.

Example:
if 10 > 5:
    print("Ten is greater")

The print statement is indented because it belongs inside the if statement. Incorrect indentation can cause an error."""
    },
    {
        "title": "Printing Output",
        "description": "Display words, numbers, and results on the screen.",
        "content": """The print() function displays information on the screen.

Example:
print("Hello, World!")
print(25)

Expected output:
Hello, World!
25

Text is usually placed inside quotation marks. Numbers can be printed without quotation marks."""
    },
    {
        "title": "Python Comments",
        "description": "Add notes to your code to make it easier to understand.",
        "content": """Comments are notes in a program. Python ignores comments when it runs the code.

Use the # symbol for a single-line comment.

Example:
# This is a comment
print("Welcome to Python")

Comments help programmers explain what a section of code does."""
    },
    {
        "title": "Variables, Constants and Database",
        "description": "Store information and understand how data can be organized.",
        "content": """A variable is a named place used to store a value.

Example:
student_name = "Alex"
age = 18

A constant is a value intended not to change. Python programmers commonly write constant names in uppercase.

Example:
PI = 3.14159

A database is an organized collection of information that can be stored, searched, and managed."""
    },
    {
        "title": "Basic Data Types in Python",
        "description": "Identify the common kinds of values used in Python.",
        "content": """Common Python data types include:

• str - text, such as "Hello"
• int - whole numbers, such as 15
• float - decimal numbers, such as 3.14
• bool - True or False values

Example:
name = "Mia"       # str
age = 16           # int
height = 1.62      # float
is_student = True # bool

The type of a value affects how Python works with it."""
    },
    {
        "title": "Arithmetic Operators and Expression",
        "description": "Perform calculations using Python operators.",
        "content": """Arithmetic operators perform mathematical operations.

+ addition       8 + 2 = 10
- subtraction    8 - 2 = 6
* multiplication 8 * 2 = 16
/ division       8 / 2 = 4.0
// floor division 17 // 5 = 3
% modulus        17 % 5 = 2
** exponent      2 ** 3 = 8

An expression combines values and operators to produce a result."""
    },
    {
        "title": "Basic Input and Output",
        "description": "Ask the user for information and display a response.",
        "content": """The input() function gets information from the user. The print() function displays information.

Example:
name = input("Enter your name: ")
print("Hello,", name)

When input() is used, the program waits for the user to type a response. The entered value is received as text (a string). Use int() or float() when a number is needed."""
    },
    {
        "title": "Conditional Statements",
        "description": "Make decisions using if, elif, and else.",
        "content": """Conditional statements let a program choose what to do based on a condition.

Example:
grade = 85

if grade >= 90:
    print("Excellent")
elif grade >= 75:
    print("Passed")
else:
    print("Failed")

Python checks the if condition first. If it is false, it checks elif. The else block runs when none of the earlier conditions are true."""
    },
    {
        "title": "Logical Operators",
        "description": "Combine or reverse conditions in a program.",
        "content": """Logical operators are used to combine conditions.

• and - True only when both conditions are True.
• or - True when at least one condition is True.
• not - reverses a Boolean result.

Example:
age = 20
has_id = True

if age >= 18 and has_id:
    print("You may enter")

Both conditions must be true for the example to display the message."""
    },
    {
        "title": "Iterations and Loops",
        "description": "Repeat instructions using for and while loops.",
        "content": """Loops repeat a block of code.

A for loop is useful when going through a sequence or a known range.

for number in range(1, 4):
    print(number)

Output:
1
2
3

A while loop repeats as long as its condition is True.

count = 1
while count <= 3:
    print(count)
    count += 1

Remember to update a while-loop condition so the loop can eventually stop."""
    }
]

questions = [
    ("Which computer operation is responsible for displaying the result to the user?", ["Input", "Processing", "Output", "Storage"], 2),
    ("Which code has correct indentation in Python?", ["if 5 > 2: print('Yes')", "if 5 > 2:\n    print('Yes')", "if 5 > 2:\nprint('Yes')", "print: if 5 > 2"], 1),
    ("What is the output of print('Python Programming')?", ["Python", "Programming", "The literal code", "Python Programming"], 3),
    ("Which symbol creates a single-line comment in Python?", ["//", "#", "**", "@"], 1),
    ("What value is stored in the variable age?  age = 18", ["age", "18", "'age'", "Nothing"], 1),
    ("Which data type is used for 3.14?", ["Integer", "String", "Float", "Boolean"], 2),
    ("What is the result of print(10 % 3)?", ["3", "1", "0", "10"], 1),
    ("Which Python function allows a user to enter information?", ["print()", "input()", "output()", "display()"], 1),
    ("Which statement runs when the if condition is false and no other condition matches?", ["if", "input", "else", "print"], 2),
    ("Which logical operator requires BOTH conditions to be True?", ["or", "not", "and", "else"], 2),
    ("What does this loop display? for x in range(1, 4): print(x)", ["1 2 3", "1 2 3 4", "0 1 2 3", "4 3 2 1"], 0),
    ("When does a while loop continue running?", ["When its condition is True", "When its condition is False", "Only once", "Only after the program closes"], 0),
    ("What is the result of print(17 // 5)?", ["3.4", "2", "3", "5"], 2),
    ("Which of these is a Boolean value?", ["'True'", "100", "2.5", "False"], 3),
    ("What is displayed when grade = 85 and the if/elif/else example from the lesson runs?", ["Excellent", "Passed", "Failed", "No output"], 1)
]

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def heading(parent, title, subtitle=""):
    tk.Label(parent, text=title, bg=BG, fg=NAVY,
             font=("Arial", 23, "bold")).pack(anchor="w", pady=(0, 5))
    if subtitle:
        tk.Label(parent, text=subtitle, bg=BG, fg=GRAY,
                 font=("Arial", 10)).pack(anchor="w", pady=(0, 18))

def make_button(parent, text, command, color=BLUE, width=22):
    return tk.Button(parent, text=text, command=command, bg=color, fg=WHITE,
                     activebackground=color, activeforeground=WHITE,
                     relief="flat", cursor="hand2", font=("Arial", 10, "bold"),
                     padx=12, pady=9, width=width)

def make_card(parent, title, description, command, number=None):
    card = tk.Frame(parent, bg=WHITE, highlightbackground="#E1E8F0",
                    highlightthickness=1, padx=16, pady=14)
    card.pack(fill="x", pady=6)
    label = f"{number}. {title}" if number else title
    tk.Label(card, text=label, bg=WHITE, fg=NAVY,
             font=("Arial", 12, "bold")).pack(anchor="w")
    tk.Label(card, text=description, bg=WHITE, fg=GRAY,
             font=("Arial", 9), wraplength=700, justify="left").pack(anchor="w", pady=5)
    tk.Button(card, text="Open lesson  →", command=command, bg=LIGHT_BLUE,
              fg=BLUE, relief="flat", cursor="hand2",
              font=("Arial", 9, "bold"), padx=10, pady=6).pack(anchor="e")
    return card

def registration_screen():
    clear_screen()
    outer = tk.Frame(root, bg=BG)
    outer.pack(expand=True)
    panel = tk.Frame(outer, bg=WHITE, padx=42, pady=35,
                     highlightbackground="#E1E8F0", highlightthickness=1)
    panel.pack()
    tk.Label(panel, text="CODE QUEST", bg=WHITE, fg=BLUE,
             font=("Arial", 25, "bold")).pack(pady=(0, 5))
    tk.Label(panel, text="Create your learning account", bg=WHITE, fg=GRAY,
             font=("Arial", 10)).pack(pady=(0, 22))
    tk.Label(panel, text="Username", bg=WHITE, fg=DARK).pack(anchor="w")
    username = tk.Entry(panel, font=("Arial", 11), width=32, relief="solid", bd=1)
    username.pack(pady=(5, 14), ipady=7)
    tk.Label(panel, text="Password", bg=WHITE, fg=DARK).pack(anchor="w")
    password = tk.Entry(panel, show="*", font=("Arial", 11), width=32, relief="solid", bd=1)
    password.pack(pady=(5, 14), ipady=7)
    tk.Label(panel, text="Confirm password", bg=WHITE, fg=DARK).pack(anchor="w")
    confirm = tk.Entry(panel, show="*", font=("Arial", 11), width=32, relief="solid", bd=1)
    confirm.pack(pady=(5, 20), ipady=7)

    def register():
        global registered_name, registered_password
        name, pw, cpw = username.get().strip(), password.get(), confirm.get()
        if not name or not pw or not cpw:
            messagebox.showwarning("Missing details", "Please complete all fields.")
        elif pw != cpw:
            messagebox.showerror("Password mismatch", "Your passwords do not match.")
        else:
            registered_name, registered_password = name, pw
            messagebox.showinfo("Account created", "Registration complete. You can now log in.")
            login_screen()

    make_button(panel, "Create Account", register, width=28).pack()
    tk.Button(panel, text="Already registered? Log in", command=login_screen,
              bg=WHITE, fg=BLUE, relief="flat", cursor="hand2").pack(pady=(12, 0))

def login_screen():
    clear_screen()
    outer = tk.Frame(root, bg=BG)
    outer.pack(expand=True)
    panel = tk.Frame(outer, bg=WHITE, padx=42, pady=35,
                     highlightbackground="#E1E8F0", highlightthickness=1)
    panel.pack()
    tk.Label(panel, text="Welcome Back", bg=WHITE, fg=NAVY,
             font=("Arial", 23, "bold")).pack(pady=(0, 5))
    tk.Label(panel, text="Log in to continue your Python journey", bg=WHITE,
             fg=GRAY, font=("Arial", 10)).pack(pady=(0, 22))
    tk.Label(panel, text="Username", bg=WHITE, fg=DARK).pack(anchor="w")
    username = tk.Entry(panel, font=("Arial", 11), width=32, relief="solid", bd=1)
    username.pack(pady=(5, 14), ipady=7)
    tk.Label(panel, text="Password", bg=WHITE, fg=DARK).pack(anchor="w")
    password = tk.Entry(panel, show="*", font=("Arial", 11), width=32, relief="solid", bd=1)
    password.pack(pady=(5, 20), ipady=7)

    def login():
        if username.get().strip() == registered_name and password.get() == registered_password and registered_name:
            dashboard()
        else:
            messagebox.showerror("Login failed", "Incorrect username or password. Register first if you do not have an account.")

    make_button(panel, "Log In", login, width=28).pack()
    tk.Button(panel, text="Create a new account", command=registration_screen,
              bg=WHITE, fg=BLUE, relief="flat", cursor="hand2").pack(pady=(12, 0))

def app_layout(page_title):
    clear_screen()
    sidebar = tk.Frame(root, bg=NAVY, width=220)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    tk.Label(sidebar, text="CODE QUEST", bg=NAVY, fg=WHITE,
             font=("Arial", 19, "bold")).pack(anchor="w", padx=20, pady=(28, 3))
    tk.Label(sidebar, text="PYTHON LEARNING PORTAL", bg=NAVY, fg="#B9C9E3",
             font=("Arial", 8, "bold")).pack(anchor="w", padx=20, pady=(0, 25))
    nav_items = [
        ("Dashboard", dashboard),
        ("Explore Lessons", explore_lessons),
        ("My Learning Progress", learning_progress),
        ("Discuss All Topics", discuss_all),
        ("Take the Quiz", start_quiz)
    ]
    for label, action in nav_items:
        tk.Button(sidebar, text=label, command=action, anchor="w",
                  bg=NAVY, fg=WHITE, activebackground="#29446D",
                  activeforeground=WHITE, relief="flat", cursor="hand2",
                  font=("Arial", 10), padx=20, pady=12).pack(fill="x")
    tk.Button(sidebar, text="Log Out", command=logout, anchor="w",
              bg="#203958", fg="#FFD7D7", activebackground="#29446D",
              relief="flat", cursor="hand2", font=("Arial", 10),
              padx=20, pady=12).pack(side="bottom", fill="x", pady=18)
    main = tk.Frame(root, bg=BG, padx=30, pady=26)
    main.pack(side="left", fill="both", expand=True)
    return main

def dashboard():
    main = app_layout("Dashboard")
    heading(main, "Your Learning Dashboard", f"Welcome, {registered_name}! Keep learning one topic at a time.")
    progress = len(set(completed))
    card = tk.Frame(main, bg=WHITE, padx=20, pady=18)
    card.pack(fill="x", pady=(0, 18))
    tk.Label(card, text="YOUR PROGRESS", bg=WHITE, fg=GRAY,
             font=("Arial", 9, "bold")).pack(anchor="w")
    tk.Label(card, text=f"{progress} / 11 lessons completed", bg=WHITE,
             fg=NAVY, font=("Arial", 21, "bold")).pack(anchor="w", pady=5)
    bar = tk.Canvas(card, height=12, bg="#E8EDF5", highlightthickness=0)
    bar.pack(fill="x", pady=(5, 0))
    bar.update_idletasks()
    width = max(bar.winfo_width(), 300)
    bar.create_rectangle(0, 0, width * progress / 11, 12, fill=BLUE, outline="")
    heading(main, "Continue Learning", "Choose what you want to do next.")
    actions = [
        ("Explore Lessons", "Read all 11 Python topics with examples.", explore_lessons),
        ("Discuss All Topics", "Go through the lessons in order, one by one.", discuss_all),
        ("Take the Quiz", "Answer 15 questions based on the lessons.", start_quiz),
        ("My Learning Progress", "Check which topics you have completed.", learning_progress)
    ]
    for title, desc, command in actions:
        make_card(main, title, desc, command)

def explore_lessons():
    main = app_layout("Explore Lessons")
    heading(main, "Explore Lessons", "Select a topic to read its explanation and examples.")
    canvas = tk.Canvas(main, bg=BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)
    content = tk.Frame(canvas, bg=BG)
    content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=content, anchor="nw", width=760)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    for i, lesson in enumerate(lessons, 1):
        make_card(content, lesson["title"], lesson["description"],
                  lambda n=i: show_lesson(n), i)

def show_lesson(number, back="explore"):
    lesson = lessons[number - 1]
    main = app_layout("Lesson")
    heading(main, f"Lesson {number}: {lesson['title']}", lesson["description"])
    completed.append(number)
    panel = tk.Frame(main, bg=WHITE, padx=24, pady=22)
    panel.pack(fill="both", expand=True)
    text = tk.Text(panel, wrap="word", bg=WHITE, fg=DARK, relief="flat",
                   font=("Arial", 11), padx=5, pady=5)
    text.pack(fill="both", expand=True)
    text.insert("1.0", lesson["content"])
    text.configure(state="disabled")
    buttons = tk.Frame(main, bg=BG)
    buttons.pack(fill="x", pady=15)
    make_button(buttons, "← Previous", lambda: show_lesson(max(1, number - 1)), color=NAVY).pack(side="left")
    make_button(buttons, "Back to Lessons", explore_lessons, color=GRAY).pack(side="left", padx=8)
    if number < 11:
        make_button(buttons, "Next Lesson →", lambda: show_lesson(number + 1)).pack(side="right")
    else:
        make_button(buttons, "Finish", dashboard).pack(side="right")

def learning_progress():
    main = app_layout("My Learning Progress")
    heading(main, "My Learning Progress", "Your completed topics are marked below.")
    done = set(completed)
    tk.Label(main, text=f"{len(done)} of 11 lessons completed",
             bg=BG, fg=BLUE, font=("Arial", 17, "bold")).pack(anchor="w", pady=(0, 14))
    for i, lesson in enumerate(lessons, 1):
        status = "✓ Completed" if i in done else "Not yet completed"
        color = GREEN if i in done else GRAY
        row = tk.Frame(main, bg=WHITE, padx=14, pady=11)
        row.pack(fill="x", pady=4)
        tk.Label(row, text=f"{i}. {lesson['title']}", bg=WHITE, fg=NAVY,
                 font=("Arial", 10, "bold")).pack(side="left")
        tk.Label(row, text=status, bg=WHITE, fg=color,
                 font=("Arial", 9, "bold")).pack(side="right")

def discuss_all():
    show_discussion(1)

def show_discussion(number):
    lesson = lessons[number - 1]
    main = app_layout("Discuss All Topics")
    heading(main, f"Topic {number} of 11", "Review each lesson in order.")
    completed.append(number)
    panel = tk.Frame(main, bg=WHITE, padx=24, pady=22)
    panel.pack(fill="both", expand=True)
    tk.Label(panel, text=lesson["title"], bg=WHITE, fg=NAVY,
             font=("Arial", 18, "bold"), wraplength=700).pack(anchor="w", pady=(0, 15))
    body = tk.Text(panel, wrap="word", bg=WHITE, fg=DARK, relief="flat",
                   font=("Arial", 11), padx=4, pady=4)
    body.pack(fill="both", expand=True)
    body.insert("1.0", lesson["content"])
    body.configure(state="disabled")
    nav = tk.Frame(main, bg=BG)
    nav.pack(fill="x", pady=15)
    if number > 1:
        make_button(nav, "← Previous Topic", lambda: show_discussion(number - 1), color=NAVY).pack(side="left")
    make_button(nav, "Back to Dashboard", dashboard, color=GRAY).pack(side="left", padx=8)
    if number < 11:
        make_button(nav, "Next Topic →", lambda: show_discussion(number + 1)).pack(side="right")
    else:
        make_button(nav, "Finish Review", dashboard).pack(side="right")

def start_quiz():
    global current_question, score
    current_question = 0
    score = 0
    show_question()

def show_question():
    global current_question
    main = app_layout("Python Quiz")
    if current_question >= len(questions):
        show_results()
        return
    question, options, answer = questions[current_question]
    heading(main, "Python Knowledge Quiz", f"Question {current_question + 1} of {len(questions)}")
    card = tk.Frame(main, bg=WHITE, padx=24, pady=24)
    card.pack(fill="both", expand=True)
    tk.Label(card, text=question, bg=WHITE, fg=NAVY,
             font=("Arial", 15, "bold"), wraplength=700,
             justify="left").pack(anchor="w", pady=(0, 22))
    selected_answer.set("")
    for i, option in enumerate(options):
        tk.Radiobutton(card, text=option, variable=selected_answer,
                       value=str(i), bg=WHITE, fg=DARK, activebackground=WHITE,
                       selectcolor=LIGHT_BLUE, font=("Arial", 11),
                       anchor="w", justify="left", wraplength=680).pack(fill="x", pady=8)

    def submit():
        global current_question, score
        if selected_answer.get() == "":
            messagebox.showwarning("Choose an answer", "Please select an answer before continuing.")
            return
        if int(selected_answer.get()) == answer:
            score += 1
        current_question += 1
        show_question()

    make_button(main, "Submit Answer  →", submit).pack(anchor="e", pady=15)

def show_results():
    main = app_layout("Quiz Results")
    percentage = round(score / len(questions) * 100)
    if score >= 13:
        remark = "Excellent! You mastered most of the topics."
    elif score >= 10:
        remark = "Very good! You have a good understanding."
    elif score >= 7:
        remark = "Good effort! Review the topics you find difficult."
    else:
        remark = "Keep practicing! Review the lessons and try again."
    heading(main, "Quiz Completed!", "Here is your result.")
    panel = tk.Frame(main, bg=WHITE, padx=30, pady=35)
    panel.pack(fill="x", pady=20)
    tk.Label(panel, text=f"{score} / {len(questions)}", bg=WHITE, fg=BLUE,
             font=("Arial", 38, "bold")).pack()
    tk.Label(panel, text=f"{percentage}% score", bg=WHITE, fg=GRAY,
             font=("Arial", 13)).pack(pady=5)
    tk.Label(panel, text=remark, bg=WHITE, fg=NAVY,
             font=("Arial", 12, "bold"), wraplength=650).pack(pady=15)
    make_button(main, "Try Again", start_quiz).pack(pady=5)
    make_button(main, "Back to Dashboard", dashboard, color=NAVY).pack(pady=5)

def logout():
    if messagebox.askyesno("Log out", "Are you sure you want to log out?"):
        login_screen()

registration_screen()
root.mainloop()
