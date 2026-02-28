""" The main script for all calculations """

# Necessary imports
import models.problems as problems
import models.circle as circle
import models.sphere as sphere
import models.semicircle as semicircle
import models.cone as cone

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
    elif problem_choice == 2:
        solution = semicircle.semi_circle()
    elif problem_choice == 3:
        solution = sphere.sphere()
    elif problem_choice == 4:
        solution = cone.cone()
    else:
        solution = print('Not yet available')

    return solution

solve()