# Python program to multiply 2 matrices

A = [ [1, 5, 7],
      [4, 0, 2],
      [6, 0, 3] ] 


B = [ [1, 0],
      [1, 0],
      [0, 0] ]

# 3x3 3x2  ----> 3x2

C = [ [0,0],
      [0,0],
      [0,0] ]


for i in range(1, len(C)):
    for j in range(1, len(C[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]
            # print (C[i][j])

for row in C:
    print(row)