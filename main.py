""" The main script for all operations """

# Necessary imports
import models.problems as problems
import models.circle as circle

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
    else:
        solution = print('Not yet available')

    return solution

solve()