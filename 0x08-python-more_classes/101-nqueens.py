#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard.
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """ Check that a queen does not already exist in that y value
            Args:
                y (int): integer value
            Returns: bool (false) or bool (true)
        """
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """ Determines whether or not to reject the solution
            Args:
                x (int): integer value 1
                y (int): integer value 2
            Returns: bool (false) or bool (true)
        """
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """ Clears the answers from the point of failure on
            Args:
                x (int): integer value
        """
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """ Recursive backtracking function to find the solution
            Args:
                x (int): integer value
        """
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)
    nqueens(0)
