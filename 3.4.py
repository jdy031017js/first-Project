n = []
for i in range(int(input())):
    n = list(map(int, input().split()))
    m = sum(n[1:]) // n[0]
    a = 0
    for j in range(1,n[0]+1):
        if n[j] > m:
            a += 1
    print("%.3f%%" % (a / n[0] * 100.0))
    n.clear()
