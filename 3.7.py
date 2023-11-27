n = int(input(""))
s = 1
a = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = s
        s +=1
    if i % 2 == 1:
        a_reverse = a[i][::-1]
        for k in range(n):
            a[i][k] = a_reverse[k]

for i in range(n):
    for j in range(n):
        print(str(a[i][j]).rjust(2),end=" ")
    print("")

