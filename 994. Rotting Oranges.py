grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

freshCount = 0
rotten = []


def explore(grid, freshCount, rotten, timeInMin):
    while (len(rotten)) > 0 and freshCount > 0:

        timeInMin += 1

        for i in range(len(rotten)):
            x, y = rotten.pop(0)
            print(x, y)
            for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                newR = dx + x
                newC = dy + y
                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and (grid[newR][newC] != 0 and grid[newR][newC] != 2):
                    grid[newR][newC] = 2
                    freshCount -= 1
                    rotten.append((newR, newC))
    return timeInMin if freshCount == 0 else -1


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            rotten.append((i, j))
        elif grid[i][j] == 1:
            freshCount += 1
timePassed = explore(grid, freshCount, rotten, timeInMin=0)
print(timePassed)
