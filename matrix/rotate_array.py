
def rotate90(a):
    for row in a:
        print(row)

    row_len = len(a)
    col_len = len(a[0])

    b = [[0] * row_len for i in range(col_len) ]

    for i in range(len(a)):   
        for j in range(len(a[0])):
            new_i = j
            new_j = row_len -1 - int (i % row_len)
            b[new_i][new_j] = a[i][j]
    return b
