s = input().lower()
s_set = list(set(s))
n = [0] * len(s)
m = 0

for i in range(len(s_set)):
    n[i] = s.count(s_set[i])

if n.count(max(n)) > 1:
    print("?")
else:
    print(s_set[n.index(max(n))].upper())






