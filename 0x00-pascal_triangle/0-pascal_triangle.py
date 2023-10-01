#!/usr/bin/python3
"""Module contains the pascal triangle fuction.

Provides a pascal_triangle function that returns a representation
of the pascal triangle.
"""


def pascal_triangle(n: int) -> list[list]:
    """ Generates a representation of teh pascal's triangle.
    Args:
        n: The number of levels to generate.

    Returns:
        [] If n < 0 else a list of lists representing the triangle

    """
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
