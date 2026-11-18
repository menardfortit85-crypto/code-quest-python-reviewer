
print("==========================================")
print("                 CODE QUEST")
print("          INTERACTIVE LEARNING PORTAL")
print("==========================================")


print("\n            CREATE ACCOUNT")
print("====================================")
registered_name = input("Create username: ")

while True:
    registered_password = input("Create password: ")
    confirm_password = input("Confirm password: ")

    if registered_password == confirm_password:
        print("\nAccount registered successfully!")
        break
    else:
        print("\nPasswords do not match!")
        print("Please try again.\n")


print("\n==========================================")
print("                 STUDENT LOGIN")
print("==========================================")

while True:

    name = input("Enter username: ")
    password = input("Enter password: ")

    if name == registered_name and password == registered_password:

        print("\n==========================================")
        print("              LOGIN SUCCESSFUL")
        print("==========================================")
        print("Welcome to CODE QUEST,", name)
        break

    else:
        print("\nIncorrect username or password!")
        print("Please try again.\n")


lessons = {

1: """
==========================================
       1. INTRODUCTION TO COMPUTING
==========================================

DEFINITION:
Computing is the process of using computers
to solve problems, process information,
and perform different tasks.

FOUR BASIC FUNCTIONS:

1. INPUT
   Data entered into a computer.

2. PROCESS
   The computer works on the data.

3. OUTPUT
   The result produced by the computer.

4. STORAGE
   Saving information for future use.

EXAMPLE:
A calculator receives numbers, processes
them, and displays the answer.

PYTHON EXAMPLE:

number1 = 10
number2 = 5
answer = number1 + number2

print(answer)

OUTPUT:
15

IMPORTANCE:
- Makes work faster.
- Helps people communicate.
- Stores information.
- Solves different problems.

REMEMBER:
A computer accepts input, processes data,
produces output, and stores information.
""",

2: """
==========================================
             2. PYTHON BASIC SYNTAX
==========================================

DEFINITION:
Python syntax refers to the rules and
structure used when writing Python programs.

IMPORTANT CONCEPTS:

1. KEYWORDS
   Reserved words such as if, else,
   while, and for.

2. IDENTIFIERS
   Names given to variables and functions.

3. INDENTATION
   Spaces used to organize blocks of code.

4. STATEMENTS
   Instructions written in a program.

5. CASE SENSITIVITY
   Uppercase and lowercase letters
   are treated differently.

EXAMPLE:

name = "Menard"

if name == "Menard":
    print("Welcome!")

OUTPUT:
Welcome!

REMEMBER:
Correct syntax helps Python understand
your instructions.
""",

3: """
==========================================
              3. PRINTING OUTPUT
==========================================

DEFINITION:
Printing output means displaying
information on the computer screen.

Python uses the print() function.

USES:
- Displaying text.
- Displaying numbers.
- Displaying variables.
- Showing calculations.

EXAMPLE 1:

print("Hello World!")

OUTPUT:
Hello World!

EXAMPLE 2:

name = "Menard"
age = 18

print(name)
print(age)

OUTPUT:
Menard
18

REMEMBER:
Text needs quotation marks, while numbers
can be printed without quotation marks.
""",

4: """
==========================================
              4. PYTHON COMMENTS
==========================================

DEFINITION:
Comments are notes written inside a program
to explain what the code does.

Python ignores comments during execution.

TYPES:

1. SINGLE-LINE COMMENT
   Uses the # symbol.

   Example:
   # This is a comment

2. MULTI-LINE NOTES
   Can be written using triple quotation
   marks.

EXAMPLE:

# Display a welcome message
print("Welcome to Code Quest!")

OUTPUT:
Welcome to Code Quest!

IMPORTANCE:
- Explains complicated code.
- Helps programmers understand programs.
- Makes code easier to read.

REMEMBER:
Comments help explain and organize code.
""",

5: """
==========================================
     5. VARIABLES, CONSTANTS AND DATABASE
==========================================

A. VARIABLES

Variables are names used to store data.
Their values can change.

EXAMPLE:

name = "Menard"
age = 18

print(name)
print(age)

OUTPUT:
Menard
18

B. CONSTANTS

Constants represent values programmers
intend to keep unchanged.

Python conventionally uses uppercase names.

EXAMPLE:

PI = 3.14159

C. DATABASE

A database is an organized collection
of information.

EXAMPLES:
- Student records
- Grades
- Attendance
- Personal information

REAL-LIFE APPLICATION:
Schools use databases to manage
student information.

REMEMBER:
Variables store values, constants represent
unchanged values, and databases organize data.
""",

6: """
==========================================
         6. BASIC DATA TYPES IN PYTHON
==========================================

DEFINITION:
Data types identify the kind of information
stored in a variable.

FOUR BASIC DATA TYPES:

1. INTEGER (int)
   Whole numbers.
   Example: age = 18

2. FLOAT (float)
   Decimal numbers.
   Example: price = 99.50

3. STRING (str)
   Text and characters.
   Example: name = "Menard"

4. BOOLEAN (bool)
   True or False.
   Example: passed = True

PYTHON EXAMPLE:

age = 18
price = 99.50
name = "Menard"
passed = True

print(type(age))
print(type(price))
print(type(name))
print(type(passed))

OUTPUT:

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

TYPE CONVERSION:

int() - Converts to an integer.
float() - Converts to a decimal.
str() - Converts to text.
bool() - Converts to Boolean.

REMEMBER:
Data types identify the kind of data
used in a program.
""",

7: """
==========================================
    7. ARITHMETIC OPERATORS AND EXPRESSION
==========================================

DEFINITION:
Arithmetic operators perform mathematical
calculations.

SEVEN OPERATORS:

1. + Addition
2. - Subtraction
3. * Multiplication
4. / Division
5. % Modulus
6. // Floor Division
7. ** Exponentiation

EXAMPLE:

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(2 ** 3)

OUTPUT:

15
5
50
2.0
0
2
8

EXPRESSION:
An expression combines values, variables,
and operators to produce a result.

REMEMBER:
Arithmetic operators help computers
perform mathematical calculations.
""",

8: """
==========================================
         8. BASIC INPUT AND OUTPUT
==========================================

DEFINITION:
Input and output allow users to interact
with computer programs.

INPUT:
Information entered by the user.

Python uses input() to receive information.

OUTPUT:
Information displayed on the screen.

Python uses print() to display information.

EXAMPLE:

name = input("Enter your name: ")

print("Hello", name)

OUTPUT:

Enter your name: Menard
Hello Menard

NUMERIC INPUT:

age = int(input("Enter age: "))

print("Your age is", age)

OUTPUT:

Enter age: 18
Your age is 18

IMPORTANT FUNCTIONS:

input() - Receives information.
print() - Displays information.
int() - Converts to a whole number.
float() - Converts to a decimal.

REMEMBER:
Input receives data and output displays it.
""",

9: """
==========================================
          9. CONDITIONAL STATEMENTS
==========================================

DEFINITION:
Conditional statements allow programs
to make decisions based on conditions.

THREE TYPES:

1. IF
   Executes code when a condition is True.

2. ELIF
   Checks another condition if the
   previous condition is False.

3. ELSE
   Executes when previous conditions
   are False.

EXAMPLE:

grade = 90

if grade >= 90:
    print("Excellent")
elif grade >= 75:
    print("Passed")
else:
    print("Failed")

OUTPUT:
Excellent

COMPARISON OPERATORS:

== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

REMEMBER:
Conditional statements help programs
make decisions.
""",

10: """
==========================================
             10. LOGICAL OPERATORS
==========================================

DEFINITION:
Logical operators combine or reverse
conditions in a Python program.

THREE TYPES:

1. AND
   Both conditions must be True.

2. OR
   At least one condition must be True.

3. NOT
   Reverses the result.

EXAMPLE - AND:

print(10 > 5 and 8 > 3)

OUTPUT:
True

EXAMPLE - OR:

print(10 < 5 or 8 > 3)

OUTPUT:
True

EXAMPLE - NOT:

print(not(10 > 5))

OUTPUT:
False

REAL-LIFE EXAMPLE:

age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")

OUTPUT:
Access granted

REMEMBER:
AND requires both, OR requires one,
and NOT reverses a condition.
""",

11: """
==========================================
           11. ITERATIONS AND LOOPS
==========================================

DEFINITION:
Loops repeat instructions automatically
without writing the same code repeatedly.

TWO MAIN TYPES:

1. FOR LOOP
   Repeats code over a sequence or range.

EXAMPLE:

for number in range(1, 6):
    print(number)

OUTPUT:

1
2
3
4
5

2. WHILE LOOP
   Repeats while a condition is True.

EXAMPLE:

count = 1

while count <= 5:
    print(count)
    count += 1

OUTPUT:

1
2
3
4
5

OTHER LOOP STATEMENTS:

BREAK:
Stops the loop immediately.

CONTINUE:
Skips the current iteration.

REMEMBER:
Loops make programs more efficient
by repeating instructions automatically.
"""

}


# LEARNING PROGRESS

completed = []


# QUIZ QUESTIONS

quiz_questions = [

    {
        "question": "1. What are the four basic functions of a computer?",
        "choices": [
            "A. Input, Process, Output, Storage",
            "B. Print, Scan, Copy, Delete",
            "C. Open, Close, Save, Run",
            "D. Keyboard, Mouse, Monitor, CPU"
        ],
        "answer": "A"
    },

    {
        "question": "2. What is indentation in Python?",
        "choices": [
            "A. A type of variable",
            "B. Spaces used to organize blocks of code",
            "C. A mathematical operator",
            "D. A command for displaying output"
        ],
        "answer": "B"
    },

    {
        "question": "3. Which Python function displays information on the screen?",
        "choices": [
            "A. input()",
            "B. type()",
            "C. print()",
            "D. int()"
        ],
        "answer": "C"
    },

    {
        "question": "4. Which symbol is used for a single-line comment?",
        "choices": [
            "A. //",
            "B. #",
            "C. **",
            "D. @"
        ],
        "answer": "B"
    },

    {
        "question": "5. What is the main purpose of a variable?",
        "choices": [
            "A. To display pictures",
            "B. To store data",
            "C. To stop a program",
            "D. To create comments"
        ],
        "answer": "B"
    },

    {
        "question": "6. What data type is the value 99.50?",
        "choices": [
            "A. Integer",
            "B. String",
            "C. Boolean",
            "D. Float"
        ],
        "answer": "D"
    },

    {
        "question": "7. What is the result of 10 % 3?",
        "choices": [
            "A. 3",
            "B. 1",
            "C. 0",
            "D. 10"
        ],
        "answer": "B"
    },

    {
        "question": "8. Which function receives information from the user?",
        "choices": [
            "A. print()",
            "B. input()",
            "C. type()",
            "D. bool()"
        ],
        "answer": "B"
    },

    {
        "question": "9. Which statement runs when the if and elif conditions are False?",
        "choices": [
            "A. for",
            "B. while",
            "C. else",
            "D. input"
        ],
        "answer": "C"
    },

    {
        "question": "10. Which logical operator requires BOTH conditions to be True?",
        "choices": [
            "A. OR",
            "B. NOT",
            "C. AND",
            "D. ELSE"
        ],
        "answer": "C"
    },

    {
        "question": "11. What is the output of print(2 ** 3)?",
        "choices": [
            "A. 5",
            "B. 6",
            "C. 8",
            "D. 9"
        ],
        "answer": "C"
    },

    {
        "question": "12. What numbers are produced by range(1, 6)?",
        "choices": [
            "A. 1, 2, 3, 4, 5",
            "B. 1, 2, 3, 4, 5, 6",
            "C. 0, 1, 2, 3, 4, 5",
            "D. 6, 5, 4, 3, 2, 1"
        ],
        "answer": "A"
    },

    {
        "question": "13. Which data type represents True or False?",
        "choices": [
            "A. int",
            "B. float",
            "C. str",
            "D. bool"
        ],
        "answer": "D"
    },

    {
        "question": "14. What does the break statement do inside a loop?",
        "choices": [
            "A. Repeats the loop",
            "B. Stops the loop immediately",
            "C. Skips all variables",
            "D. Displays a message"
        ],
        "answer": "B"
    },

    {
        "question": "15. When does a while loop continue executing?",
        "choices": [
            "A. When its condition is True",
            "B. When its condition is False",
            "C. Only when the user logs in",
            "D. Only once"
        ],
        "answer": "A"
    }

]


# QUIZ SYSTEM

def take_quiz():

    score = 0

    print("\n==========================================")
    print("              CODE QUEST QUIZ")
    print("==========================================")
    print("             15 QUESTIONS")
    print("==========================================")

    print("\nInstructions:")
    print("Choose the correct answer: A, B, C, or D.")
    print("Answer all 15 questions.")

    input("\nPress Enter to start the quiz...")

    for question in quiz_questions:

        print("\n------------------------------------------")
        print(question["question"])
        print("------------------------------------------")

        for choice in question["choices"]:
            print(choice)

        while True:

            answer = input("\nYour answer: ").upper().strip()

            if answer in ["A", "B", "C", "D"]:
                break

            else:
                print("Invalid answer!")
                print("Please choose A, B, C, or D.")

        if answer == question["answer"]:

            print("\nCorrect answer!")
            score += 1

        else:

            print("\nIncorrect answer!")
            print("Correct answer:", question["answer"])

        input("\nPress Enter for the next question...")

    percentage = (score / 15) * 100

    print("\n==========================================")
    print("               QUIZ RESULTS")
    print("==========================================")

    print("Student:", name)
    print("Correct Answers:", score, "/ 15")
    print("Percentage:", round(percentage, 2), "%")

    if score >= 13:

        print("\nREMARK: EXCELLENT!")
        print("You mastered most of the topics.")

    elif score >= 10:

        print("\nREMARK: VERY GOOD!")
        print("You have a good understanding.")

    elif score >= 7:

        print("\nREMARK: GOOD EFFORT!")
        print("Review the topics you find difficult.")

    else:

        print("\nREMARK: KEEP PRACTICING!")
        print("Review the lessons and try again.")

    print("\n==========================================")

    input("\nPress Enter to return to dashboard...")


# MAIN DASHBOARD

while True:

    print("\n==========================================")
    print("              CODE QUEST DASHBOARD")
    print("==========================================")

    print("Student:", name)
    print("Completed Lessons:", len(completed), "/ 11")

    print("\n1. Explore Lessons")
    print("2. My Learning Progress")
    print("3. Discuss All Topics")
    print("4. Take the Quiz")
    print("5. Logout")

    print("==========================================")

    option = input("Select an option: ")


    if option == "1":

        while True:

            print("\n==========================================")
            print("                EXPLORE LESSONS")
            print("==========================================")

            print("1. Introduction to Computing")
            print("2. Python Basic Syntax")
            print("3. Printing Output")
            print("4. Python Comments")
            print("5. Variables, Constants and Database")
            print("6. Basic Data Types in Python")
            print("7. Arithmetic Operators and Expression")
            print("8. Basic Input and Output")
            print("9. Conditional Statements")
            print("10. Logical Operators")
            print("11. Iterations and Loops")
            print("12. Back to Dashboard")

            print("==========================================")

            topic = input("Choose a lesson: ")

            if topic.isdigit() and 1 <= int(topic) <= 11:

                topic_number = int(topic)

                print(lessons[topic_number])

                if topic_number not in completed:
                    completed.append(topic_number)

                print("Lesson completed!")

                input("\nPress Enter to return to lessons...")

            elif topic == "12":
                break

            else:
                print("Invalid lesson selection!")


    elif option == "2":

        print("\n==========================================")
        print("             MY LEARNING PROGRESS")
        print("==========================================")

        print("Student:", name)
        print("Completed:", len(completed), "out of 11")

        for number in range(1, 12):

            if number in completed:
                status = "COMPLETED"
            else:
                status = "NOT YET COMPLETED"

            print("Lesson", number, "-", status)

        if len(completed) == 11:
            print("\nCONGRATULATIONS!")
            print("You completed all lessons!")

        input("\nPress Enter to return to dashboard...")


    elif option == "3":

        print("\nSTARTING COMPLETE LESSON DISCUSSION")

        for number in range(1, 12):

            print(lessons[number])

            if number not in completed:
                completed.append(number)

            input("\nPress Enter for the next lesson...")

        print("\nYou finished all discussions!")

        input("\nPress Enter to return to dashboard...")


    elif option == "4":

        take_quiz()


    elif option == "5":

        print("\n==========================================")
        print("                SESSION ENDED")
        print("==========================================")

        print("Thank you for using CODE QUEST!")
        print("Keep learning and improving,", name)
        print("Goodbye!")

        break


    else:

        print("\nInvalid option! Please try again.")

