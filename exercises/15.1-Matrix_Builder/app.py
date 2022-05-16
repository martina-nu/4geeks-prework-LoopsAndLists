def matrixBuilder(x):
    rows, cols = (x, x)
    arr = [[1 for i in range(cols)] for j in range(rows)]
    return arr
    
print(matrixBuilder(3))