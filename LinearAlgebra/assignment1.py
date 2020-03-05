import math

matrix_a = [[-1, 2, 0], [2, 0, 3]]
matrix_b = [[2, 0, -1], [1, -2, 0]]
matrix_c = [[0, 2], [1, 0], [-1, 1]]
matrix_e = [[2, -1], [math.pi, math.log10(2)], [-2, 6]]
matrix_i = [[1, 0], [0, 1]]

def matrix_add(matrix_x, pow_x, matrix_y, pow_y):
    rows_x = len(matrix_x)
    rows_y = len(matrix_y)
    if not rows_x == rows_y:
        return None
    cols_x = len(matrix_x[0])
    cols_y = len(matrix_y[0])
    if not cols_x == cols_y:
        return None

    matrix_sum = [[0]*cols_x]*rows_x
    for i in range(len(matrix_x)):
        for j in range(len(matrix_x[0])):
            matrix_sum[i][j] = matrix_x[i][j]*pow_x + matrix_y[i][j]*pow_y
    return matrix_x

def matrix_mutiply(matrix_x, matrix_y):
    print("Not implemented")

def matrix_transpose(matrix_input):
    rows = len(matrix_input)
    cols = len(matrix_input[0])
    matrix_output = []
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(matrix_input[j][i])
        matrix_output.append(temp)

    return matrix_output

def problem_a():
    global matrix_a, matrix_b, matrix_c, matrix_e
    
    a1 = matrix_add(matrix_a, 1, matrix_b, 2)
    print("A + 2B =", a1)

    a2 = matrix_add(matrix_c, 1, matrix_e, -1)
    print("C - E =", a2)

    print("A ^ T =", matrix_transpose(matrix_a))


def main():
    problem_a()

if __name__ == "__main__":
    main()