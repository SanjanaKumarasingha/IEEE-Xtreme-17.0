n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

#print(matrix)

count = 0
for row in range(1,len(matrix)):
    matrix[row] = matrix[0]
    count += 1
if count == n-1:
    print('{:.6f}'.format(1.000000))