# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from random import randint, choice

def answer_check(correct_answer):
    print()
    try:
        result = float(input("\tWhat's your answer? >> "))
        if abs(result - correct_answer) <= 0.05:
            print(f'\tCorrect! The answer is: {correct_answer}')
        else:
            print(f'\tSorry, wrong.  The correct answer is: {correct_answer}.')
    except ValueError:
        print("\tSorry, that wasn't a valid input.")
    print()
    input('\tPress any key to continue...')

def multiplication():
    print('\tCalculate the following:')
    multiplier = randint(0,99)
    multiplicand = randint(0,9000)
    correct_answer = multiplier * multiplicand
    print(f'\tShow the product of:\t {multiplier} x {multiplicand}')
    answer_check(correct_answer)

def division():
    print('\tCalculate the following:')
    dividend = randint(0,9000)
    divisor = randint(1,12)
    correct_answer = dividend / divisor
    print(f'\tShow the quotient of:\t {dividend} / {divisor}')
    answer_check(correct_answer)

def negatives():
    print('\tCalculate the following:')
    num1 = randint(-20, +20)
    num2 = randint(-10, +10)
    sign = choice('+-*/')
    correct_answer_str = str(num1) + sign + str(num2)
    correct_answer = eval(correct_answer_str)
    print(f'\tShow the result of:\t {num1} {sign} {num2}')
    answer_check(correct_answer)

def ttables():
    print('\tCalculate the following:')
    num1 = randint(1,12)
    num2 = randint(1,12)
    correct_answer = num1 * num2
    print(f'\tShow the result of:\t {num1} * {num2}')
    answer_check(correct_answer)

def squares():
    squares_dict = {1:1, 4:2, 9:3, 16:4, 25:5, 36:6, 49:7, 64:8, 81:9, 100:10, 121:11, 144:12, 169:13, 196:14, 225:15}
    question, correct_answer = choice(list(squares_dict.items()))
    print(f'\tWhat is the Square Root of: {question}')
    answer_check(correct_answer)

def cubes():
    cubes_dict = {1:1, 8:2, 27:3, 64:4, 125:5, 216:6, 343:7, 512:8, 729:9, 1000:10, 1331:11, 1728:12, 2197:13, 2744:14}
    question, correct_answer = choice(list(cubes_dict.items()))
    print(f'\tWhat is the Cube Root of: {question}')
    answer_check(correct_answer)


# Create the menu
menu = ConsoleMenu("GCSE Maths", "Test Me")

# Create some items

# A FunctionItem runs a Python function when selected
# function_item = FunctionItem("Call a Python function", input, ["Enter an input: "])
multiply = FunctionItem("Multiplications", multiplication)
divide = FunctionItem("Divisions", division)
negative = FunctionItem("Negative Numbers", negatives)
tables = FunctionItem("Times Tables", ttables)
squares = FunctionItem("First 15 Squares", squares)
cubes = FunctionItem("First 15 Cubes", cubes)

# menu.append_item(menu_item)
menu.append_item(multiply)
menu.append_item(divide)
menu.append_item(negative)
menu.append_item(tables)
menu.append_item(squares)
menu.append_item(cubes)

# Finally, we call show to show the menu and allow the user to interact
menu.show()