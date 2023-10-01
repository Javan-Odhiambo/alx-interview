#!/usr/bin/python3
'''Pascal's triangle'''


def pascal_triangle(n: int) -> list[list]:
    '''Returns a Pascal's Triangle representation'''
    if n < 1:
        return []

    solution = [[1]]
    results = [1]

    for i in range(n-1):
        temp = [0] + results + [0]
        results = []
        for j in range(len(temp) - 1):
            results.append(temp[j] + temp[j+1])

        solution.append(results)

    return solution
