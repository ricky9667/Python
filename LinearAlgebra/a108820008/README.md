## Linear Algebra Assignment 
### By 108820008 電資一 胡紹宇

### Functions

- `print_matrix(matrix)`
    - prints out formatted matrix list
    - returns `"Matrix undefined"` if `matrix == None`

```python
matrix = [[1, 0], [2, 3]]
print_matrix(matrix)

# result
[1, 0]
[2, 3]
```

- `matrix_add(x, times_x, y, times_y):`
    - adds 2 matrices with same size
    - returns `None` when addition unavailable (different sizes, etc.)

```python
x = [[1, 0], [2, 3]]
y = [[3, 4], [1, 7]]
add = matrix_add(x, 1, y, 2) # add = x + 2y
print_matrix(add)

# result
[7, 8]
[4, 17]

x = [[1, 0], [2]]
y = [[3, 4], [1, 7, 4]]
add = matrix_add(x, 1, y, 1)
print_matrix(add)

# result 
"Matrix undefined" # add == None
```

- `matrix_transpose(matrix)`
    - transposes a matrix

```python
x = [[1, 0], [4, 3], [7, 2]]
print_matrix(x)

# result
[1, 0]
[4, 3]
[7, 2]

tx = matrix_transpose(x)
print_matrix(tx)

# result
[1, 4, 7]
[0, 3, 2]
```

- `matrix_mutiply(matrix_x, matrix_y)`
    - multiplies 2 matrices
    - returns `None` if sizes are not compatible

```python
x = [[-1, 2, 0], [2, 0, 3]]
y = [[0, 2], [1, 0], [-1, 1]]
mul = matrix_multiply(x, y)
print_matrix(mul)

# result
[2, -2]
[-3, 7]

x = [[-1, 2, 0], [2, 0, 3]]
y = [[0, 2], [1, 0]]
mul = matrix_multiply(x, y)
print_matrix(mul)

# result
"Matrix undefined"
```

- `matrix_inverse(matrix)`
    - supports only **2 dimensional** matrices
    - calculates the inverse of a matrix
    - returns `None` if matrix is unable to convert (`ad - bc == 0`)

```python
x = [[2, -2], [-3, 7]]
ix = matrix_inverse(x)
print_matrix(ix)

# result
[0.875, 0.25]
[0.375, 0.25]

x = [[1, 3], [2, 6]]
ix = matrix_inverse(x)
print_matrix(ix)

# result 
"Matrix undefined"
```
