""" The main script for all operations """

# Necessary imports
import models.problems as problems
import models.circle as circle
import models.sphere as sphere

# Welcome text
print('\n\n')
print("=" * 50)
print("\n\tWelcome to the area calculator app\n")
print("=" * 50)

# User chooses the problem
problem_choice = problems.available_problems()

# Function that solves the problems
def solve():
    if problem_choice == 1:
        solution = circle.circle()
    elif problem_choice == 3:
        solution = sphere.sphere()
    else:
        solution = print('Not yet available')

    return solution

solve()