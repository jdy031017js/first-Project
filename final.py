# 4.7
import random
import turtle

while True:
    a = int(random.randint(1,9))
    b = int(random.randint(1,9))
    an = int(input("{} X {} = ".format(a,b)))
    if a * b == an :
        print('잘했어요')
    else :
        print('틀렸어요')


for i in range(5):
    print(i)
    print(i ** 2)

for i in range(0, 10, 2):
    print(i)
    # 0부터 10까지 2만큼 증가

t = turtle.Turtle()
for i in range(0, 10, 2):
    t.circle(100)
    t.left(72)

t.clear()
i = 0
while i < 5:
    t.cirle(100)
    t.right(360 / 5)
    i = i + 1
name = 'hanna'

print('hello {}'.format(name))

# hello hanna
a = 10

b = 20

s = a + b

print('{} + {} = {}'.format(a, b, s))

# 10 + 20 = 30
print('{0} + {1} = {2}'.format(a, b, s))
print('{0} + {0} = {0}'.format(a, b, s))
# a만 출력 10 + 10 = 20

pi = 3.1415926

r = 5

print('원의 넓이는 = %f * %d = %f', pi, r, pi * r * r)

pi = 3.1415926

r = 5
print('{0}*{1}^2 = {2}'.format(pi, r, pi * r * r))

A, B = input().split()
if A<B :
    print("<")
elif A>B :
    print(">")
else :
    print("==")

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.fd(dist)
t.left(135)
t.fd(gist)
t.left(135)
t.fd(dist)

c =int(input('C :'))
f = (9/5) * c +32

for i in range(5):
    print("\n")
    print("섭씨   화씨")
    print(str(c).rjust(3) ," ",str(f).rjust(5))
    print("\n")
    c =int(input('C :'))
    f = (9/5) * c +32

