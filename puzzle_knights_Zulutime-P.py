from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge0 = And(
    Implication(Symbol('A'), And(Symbol('A'), Not(Symbol('A'))))
)

knowledge1 = And(
    Implication(Symbol('A'), And(Not(Symbol('A')), Not(Symbol('B')))),
    Symbol('B')
)

knowledge2 = And(
    Biconditional(Symbol('A'), Symbol('B')),
    Biconditional(Not(Symbol('A')), Not(Symbol('B')))
)

knowledge3 = Or(
    And(
        Implication(Symbol('A'), Symbol('A')),
        Implication(Not(Symbol('A')), Not(Symbol('A')))
    ),
    And(
        Implication(Symbol('B'), Not(Symbol('A'))),
        Implication(Not(Symbol('B')), Symbol('A')),
        Implication(Symbol('B'), Not(Symbol('C'))),
        Implication(Not(Symbol('B')), Symbol('C')),
        Implication(Symbol('C'), Symbol('A')),
        Implication(Not(Symbol('C')), Not(Symbol('A')))
    )
)

queries = [
    (knowledge0, Symbol('A')),
    (knowledge1, And(Symbol('A'), Symbol('B'))),
    (knowledge2, And(Symbol('A'), Symbol('B'))),
    (knowledge3, And(Or(Symbol('A'), Not(Symbol('A'))), Symbol('C')))
]

for i, (knowledge, query) in enumerate(queries):
    result = model_check(knowledge, query)
    print(f"Puzzle {i}:", "Entailed" if result else "Not Entailed")
