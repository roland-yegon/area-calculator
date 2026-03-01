""" The main script for all calculations """

# Necessary imports
import models.problems as problems
import models.circle as circle
import models.sphere as sphere
import models.semicircle as semicircle
import models.cone as cone
import models.triangle as triangle
import models.rectangle as rectangle
import models.square as square
import models.rhombus as rhombus
import models.parallelogram as parallelogram
import models.trapezium as trapezium


# Welcome text
print('\n\n')
print("=" * 50)
print("\n\tWelcome to the area calculator app\n")
print("=" * 50)

# Function that solves the problems
def solve():
    while True:
        # User chooses the problem
        problem_choice = problems.available_problems()

        # Solves the problem based on the user's choice
        if problem_choice == 1:
            solution = circle.circle()
        elif problem_choice == 2:
            solution = semicircle.semi_circle()
        elif problem_choice == 3:
            solution = sphere.sphere()
        elif problem_choice == 4:
            solution = cone.cone()
        elif problem_choice == 5:
            solution = triangle.triangle()
        elif problem_choice == 6:
            solution = rectangle.rectangle()
        elif problem_choice == 7:
            solution = square.square()
        elif problem_choice == 8:
            solution = rhombus.rhombus()
        elif problem_choice == 9:
            solution = parallelogram.parallelogram()
        elif problem_choice == 10:
            solution =trapezium.trapezium()
        else:
            solution = print('Exiting the program...\n\n')   
            break

        # Try again
        choices = ['y', 'n']
        choice = None

        while choice not in choices:
            choice = input("Do you want to solve another problem? (y/n): ")
        
        if choice.lower() != 'y':
            print('Exiting the program...\n\n')
            break
        else:
            print('\n\nYou stayed!!!\n')

    return solution

solve()