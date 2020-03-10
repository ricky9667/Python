# Linear Algebra Assignment 
### By 108820008 電資一 胡紹宇

### Functions

- print_matrix(matrix)
    - prints out formatted matrix list
    - returns `"Matrix undefined"` if `matrix == None`

```python
matrix = [[1, 0], [2, 3]]
print_matrix(matrix)

# result
[1, 0]
[2, 3]
```

- matrix_add(x, timeys_x, y, times_y):
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




