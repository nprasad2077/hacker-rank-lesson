matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
matrix2 = [[1, 2],[3, 4]]


def flippingMatrix(matrix):
    matrixSum = []
    middle = len(matrix) // 2

    for i in range(middle):
        for j in range(middle):
            matrixSum.append(max(matrix[i][j], matrix[i][~j], matrix[~i][j], matrix[~i][~j]))
    print(sum(matrixSum))
    return(sum(matrixSum))





def flippingMatrix2(matrix):
    matrixSum = []
    middle = len(matrix) // 2

    for i in matrix:
        print(i)

    for i in range(middle):
        print(i)
        for j in range(middle):
            print(j)
            print(matrix[i][j], matrix[~i][j], matrix[i][~j], matrix[~i][~j])


# flippingMatrix2(matrix)
flippingMatrix2(matrix2)   
# print(matrix[0][-2])