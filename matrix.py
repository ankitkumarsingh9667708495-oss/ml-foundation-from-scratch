# a = [[1,2,3],
#      [3,4,5]]

# b = [[1,2],[3,4],[5,6]]

# result = [[0,0],[0,0]]

# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             result[i][j] += a[i][k]*b[k][j]

# for r in result:
#     print(r)



a = [[2,3,4],[6,7,8]]
b = [[4,5],[6,7],[8,9]]

result = [[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] = a[i][k]*b[k][j]

# print(result)

for r in result:
    print(r)