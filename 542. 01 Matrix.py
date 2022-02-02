mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

res = []


def exploreMat(mat, queue):
    for row, column in queue:
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            newR = row + dx
            newC = column + dy
            if 0 <= newR < len(mat) and 0 <= newC < len(mat[0]) and mat[newR][newC] == -1:
                mat[newR][newC] = mat[row][column] + 1
                queue.append((newR ,newC))
    return mat


queue = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            queue.append((i, j))
        else:
            mat[i][j] = -1
print(queue)
exploreMat(mat, queue)
print(mat)
