from logic import *

# Define propositions for knights and knaves for each character
A_knight, A_knave = map(exprvar, ['A_knight', 'A_knave'])
B_knight, B_knave = map(exprvar, ['B_knight', 'B_knave'])
C_knight, C_knave = map(exprvar, ['C_knight', 'C_knave'])

# Puzzle 0: A says “I am both a knight and a knave.”
knowledge0 = And(Or(A_knight, A_knave), Equivalent(A_knight, And(A_knight, A_knave)))

# Puzzle 1: A says “We are both knaves.”, B says nothing.
knowledge1 = And(
    Equivalent(A_knight, And(A_knave, B_knave)),  # A's statement
    Not(B_knight)  # B says nothing
)

# Puzzle 2: A says “We are the same kind.”, B says “We are of different kinds.”
knowledge2 = And(
    Or(And(A_knight, B_knight), And(A_knave, B_knave)),  # A's statement
    Or(And(A_knight, B_knave), And(A_knave, B_knight))  # B's statement
)

# Puzzle 3: A says either “I am a knight.” or “I am a knave.”, B says “A said ‘I am a knave.’”, B then says “C is a knave.”, C says “A is a knight.”
knowledge3 = And(
    Or(A_knight, A_knave),  # A's ambiguous statement
    Equivalent(B_knight, Not(A_knave)),  # B's first statement
    Equivalent(C_knave, B_knight),  # B's second statement about C
    Equivalent(A_knight, C_knight)  # C's statement about A
)

# Solve puzzles using model checking
def solve_puzzle(knowledge):
    solution = satisfiable(knowledge)
    if solution:
        model = solution.satisfy_one()
        for variable, value in model.items():
            print(f"{variable}: {'Knight' if value else 'Knave'}")
    else:
        print("No solution found.")

# Solve each puzzle
print("Puzzle 0:")
solve_puzzle(knowledge0)

print("\nPuzzle 1:")
solve_puzzle(knowledge1)

print("\nPuzzle 2:")
solve_puzzle(knowledge2)

print("\nPuzzle 3:")
solve_puzzle(knowledge3)
