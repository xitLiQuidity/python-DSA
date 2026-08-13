def maze_problem(maze):
    print("Original maze")

    for i in maze:
        for j in i:
            print(j, end=" ")
        print()

    row = len(maze)
    col = len(maze[0])

    result = [[0 for i in range(col)] for j in range(row)]

    # Check whether the cell is safe
    def is_safe(x, y):

        # Check boundaries
        if x < 0 or x >= row:
            return False

        if y < 0 or y >= col:
            return False

        # Check whether the cell is open
        if maze[x][y] != 1:
            return False

        return True

    def solution(x, y):

        # Destination reached
        if x == row - 1 and y == col - 1:

            if maze[x][y] != 1:
                return False

            result[x][y] = 1
            return True

        # Check whether current cell is safe
        if is_safe(x, y):

            result[x][y] = 1

            # Move right
            if solution(x, y + 1):
                return True

            # Move down
            if solution(x + 1, y):
                return True

            # Backtrack
            result[x][y] = 0

        return False

    # Start from (0,0)
    if solution(0, 0):
        return result
    else:
        return "No path found in maze"


maze = [
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1]
]

res = maze_problem(maze)

if isinstance(res, list):

    print("Resultant path:")

    for i in res:
        for j in i:
            print(j, end=" ")
        print()

else:
    print(res)
