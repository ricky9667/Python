import math

matrix_a = [[-1, 2, 0], [2, 0, 3]]
matrix_b = [[2, 0, -1], [1, -2, 0]]
matrix_c = [[0, 2], [1, 0], [-1, 1]]
matrix_e = [[2, -1], [math.pi, math.log10(2)], [-2, 6]]
matrix_f = []
matrix_g = []
matrix_i = [[1, 0], [0, 1]]

def print_matrix(matrix):
    if matrix == None:
        print("Matrix undefined")
    for row in matrix:
        print(row)
    print()

def matrix_add(matrix_x, times_x, matrix_y, times_y):
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
            temp.append(matrix_x[i][j]*times_x + matrix_y[i][j]*times_y)
        matrix_sum.append(temp)
    return matrix_sum

def matrix_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    output = []
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(matrix[j][i])
        output.append(temp)
    return output

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

def matrix_inverse(matrix):
    p = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    print(p)
    output = [[matrix[1][1]/p, -matrix[0][1]/p], [-matrix[1][0]/p, matrix[0][0]/p]]
    return output

def problem_a():
    global matrix_a, matrix_b, matrix_c, matrix_e
    print("\n========= Problem A =========\n")

    a1 = matrix_add(matrix_a, 1, matrix_b, 2)
    print("A + 2B =")
    print_matrix(a1)

    a2 = matrix_add(matrix_c, 1, matrix_e, -1)
    print("C - E =")
    print_matrix(a2)

    a3 = matrix_transpose(matrix_a)
    print("A ^ T =")
    print_matrix(a3)

    a4 = matrix_transpose(matrix_e)
    print("E ^ T =")
    print_matrix(a4)

def problem_b():
    global matrix_a, matrix_c, matrix_f
    print("\n========= Problem B =========\n")

    matrix_f = matrix_mutiply(matrix_a, matrix_c)
    print("F = A * C =")
    print_matrix(matrix_f)

    matrix_g = matrix_mutiply(matrix_c, matrix_a)
    print("G = C * A =")
    print_matrix(matrix_g)

def problem_c():
    global matrix_f
    print("\n========= Problem C =========\n")

    c1 =  matrix_inverse(matrix_f)
    print("F ^ (-1) =")
    print_matrix(c1)

    c2 = matrix_mutiply(matrix_f, matrix_inverse(matrix_f))
    print("F * F ^ (-1) =")
    print_matrix(c2)

def main():
    problem_a()
    problem_b()
    problem_c()
    print()

if __name__ == "__main__":
    main()