import math

def det2x2(equation: list[list]):
    a = equation[0][0]
    b = equation[0][1]
    c = equation[1][0]
    d = equation[1][1]

    DET = a*d - b*c
    if DET == 0:
        print("Infintely many solutons.")
    return DET


equation = [
    [2, 1, 5],
    [1, -1, 1]
]

print(det2x2(equation=equation))