matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 3


def binarySearch(matrixRow, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2

        if matrixRow[mid] > target:
            right -=1
        elif matrixRow[mid]< target:
            left +=1
        else:
            return True
    return False

for i in matrix:
    matrixRow = i
    if binarySearch(matrixRow, target, left=0, right=len(i) - 1):
        print(True)
        break
