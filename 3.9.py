s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
a_list = list(a)
n = 0
z = 0

for i in range(len(s)):
    for j in range(len(s)):
        if a[i:i+2] == s[j]:
            n += 1
            a_list[i:i+2] = ''
    if a[i:i+3] == s[2]:
        n += 1
        a_list[i:i + 3] = ''

print(a_list, n)
