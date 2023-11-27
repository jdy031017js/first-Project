A = [list(map(int, input().split())) for _ in range(9)]
M = max(list(map(max, A)))
for i in range(9):
    for j in range(9):
        if A[i][j] == M:
            print(M)
            print(i+1, j+1)
            break
