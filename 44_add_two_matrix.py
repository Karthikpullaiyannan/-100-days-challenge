matrix=[[2,3],
          [4,2]]
matrix_2=[[5,7],
          [9,24]]
c=[[0,0],[0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        c[i][j]=matrix[i][j]+matrix_2[i][j]
for i in c:
    print(i)