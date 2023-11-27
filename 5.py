import random
import turtle

# 5.1
print("1 부터 100까지의 숫자 중에서 홀수는 :")
for i in range(1, 100):
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

i = 1
print("\n")
print("while 문")
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print("\n")
print("1 부터 100까지의 숫자 중에서 짝수는 :")
for i in range(1, 100):
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

i = 1
print("\n")
print("while 문")
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

# 5.2 - 3
print("\n")
a = int(input("시작 정수를 입력 :"))
b = int(input("끝  정수를 입력 :"))
i = 0
for j in range(a, b + 1):
    i += j
    j += 1
print(" {} 에서 {} 까지 정수의 합 : {}".format(a, b, i))
print("")

# 5.3
print("메뉴")
print("1) 햄버거")
print("2) 치킨")
print("3) 피자")
a = int(input(("1 부터 3까지 메뉴를 선택하세요 : ")))
while a > 3:
    a = int(input("메뉴를 다시 입력하세요 : "))

if a == 1:
    print("햄버거를 선택하셨습니다.")
if a == 2:
    print("치킨를 선택하셨습니다.")
if a == 3:
    print("피자를 선택하셨습니다.")
print("")

# 5.4
a = int(input("숫자를 입력하시오 :"))
for i in range(0, a + 1, 1):
    print(str("*" * i).rjust(a))
print("")

# 5.5
t = turtle.Turtle()
day = 1
i, s = map(int, input("올라갈 거리와 내려온 거리를 입력하시오 :").split())
m = 7
while i <= 30:
    print("day: {:>3} 달팽이의 위치 :{:>3}미터".format(day, m))
    i += i
    i -= s
    day = day + 1
    m = i
    t.fd(m)
    turtle.dot(2, "red")
print("축하합니다. 우물을 탈출하셨습니다.")
print("우물을 탈추출하는데 걸린 날은 {}일 입니다.".format(day))
print("")

# 5.7
print("세 자리 암스트롱 수")
s = 0
t = 0
for i in range(100, 1000):
    a = i // 100
    b = (i % 100) // 10
    c = (i % 100) % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i, end=' ')
        t = t + 1
        s = s + i
print("세자리 암스트롱 수의 합은 {} 평균은 {}입니다.".format(s, s / t))
print("")

# 5.9
a = list()
i = 0
while True:
    s = int(input("정수를 입력하시오 :"))
    a.append(s)
    i = i + 1
    if min(a) == -99:
        break
del a[i - 1]
print("{} 개의 유효한 정수 중 가장 큰 정수는 {} 이고, 가장 작은 정수는 {} 입니다.".format(i, max(a), min(a)))

# 5.10
t = turtle.Turtle()
t.shape("turtle")
for i in range(0, 30, 1):
    r = random.randrange(2)
    if r == 0:
        t.left(90)
        t.fd(50)
    else:
        t.right(90)
        t.fd(50)

print ('hamma "aa"ss')
print("glaal\"gkssk\"glss") #""안에 ""넣는 법


