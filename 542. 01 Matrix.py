mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

res = []


def exploreMatrix(mat, r, c, destination):
    rowInbound = 0<= r < len(mat)
    colInbound = 0<= c < len(mat[0])

    if not rowInbound or colInbound :
        return False
    queue = [[ r,c, 0]]

    while len(queue)>0:
        top = queue.pop(0)

        if top[0] == destination:
            return top[1]
        exploreMatrix(mat , r-1 ,c , destination)
        exploreMatrix(mat , r+1 , c ,destination)
        exploreMatrix(mat , r , c-1 , destination)
        exploreMatrix(mat , r , c+1 , destination)


for i in range(len(mat)):
    for j in range(len(mat[0])):
        exploreMatrix(mat , i ,j , destination = 0)

