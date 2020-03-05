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

    matrix_sum = []
    for i in range(len(matrix_x)):
        temp = []
        for j in range(len(matrix_x[0])):
            temp.append(matrix_x[i][j]*pow_x + matrix_y[i][j]*pow_y)
        matrix_sum.append(temp)
    return matrix_sum

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

def matrix_mutiply(matrix_x, matrix_y):
    rows_x = len(matrix_x)
    cols_x = len(matrix_x[0])
    rows_y = len(matrix_y)
    cols_y = len(matrix_y[0])
    if not cols_x == rows_y:
        return None
    
    rows_mul, cols_mul, mul_len = rows_x, cols_y, cols_x
    matrix_mul = []
    for i in range(rows_mul):
        row = []
        for j in range(cols_mul):
            element = 0
            for p in range(mul_len):
                element += matrix_x[i][p] * matrix_y[p][j]
            row.append(element)
        matrix_mul.append(row)
    return matrix_mul

def problem_a():
    global matrix_a, matrix_b, matrix_c, matrix_e
    print("\n========= Problem A =========\n")

    a1 = matrix_add(matrix_a, 1, matrix_b, 2)
    print("A + 2B =", a1)
    a2 = matrix_add(matrix_c, 1, matrix_e, -1)
    print("C - E =", a2)
    print("A ^ T =", matrix_transpose(matrix_a))
    print("E ^ T =", matrix_transpose(matrix_e))
    
    print("\n=============================\n")

def problem_b():
    global matrix_a, matrix_c
    print("\n========= Problem B =========\n")
    print("F = A * C =", matrix_mutiply(matrix_a, matrix_c))
    print("F = C * A =", matrix_mutiply(matrix_c, matrix_a))
    print("\n=============================\n")

def main():
    problem_a()
    problem_b()

if __name__ == "__main__":
    main()