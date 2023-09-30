matrix_1=[[20,3,40],
          [54,69,4],
          [6,78,43]]
matrix_2=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        matrix_2[j][i]=matrix_1[i][j]
for i in matrix_2:
    print(i)