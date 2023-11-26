def menu():
    print("1 : 정삼각형")
    print("2 : 정사각형")
    print("3 : 직사각형")
    print("4 : 평행사변형")
    print("5 : 원")
    print("6 : 사다리꼴")
    n = int(input("\n메뉴를 선택하세요:"))
    print("\n")
    return n

def Color():
    x, y = map(int, input("지정 좌표(x, y)를 입력하시오:").split())
    c = input("색깔을 입력하시오:")
    t.pu()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.begin_fill()
    
def Tri():
    Color()
    z = int(input("정삼각형의 변을 입력하시오:"))
    for i in range(3):
        t.fd(z)
        t.lt(120)
    t.end_fill()
    
def Squre1():   
    Color()
    z = int(input("정사각형의 변을 입력하시오:"))
    for i in range(4):
        t.fd(z)
        t.lt(90)
    t.end_fill()
   
def Squre2():   
    Color()
    z1, z2 = map(int, input("직사각형의 가로, 세로를 입력하시오:").split())
    for i in range(2):
        t.fd(z1)
        t.lt(90)
        t.fd(z2)
        t.lt(90)
    t.end_fill()

def Squre3():
    Color()
    z1, z2 = map(int, input("평행사변형의 가로, 세로를 입력하시오:").split())
    for i in range(2):
        t.fd(z1)
        t.lt(60)
        t.fd(z2)
        t.lt(120)
    t.end_fill()

def Circle():
    Color()
    z = int(input("원의 반지름을 입력하시오:"))
    t.circle(z)
    t.end_fill()

def Squre4():
    Color()
    z1, z2, z3 = map(int, input("사다리꼴의 가로, 세로, 빗변을 입력하시오:").split())
    t.fd(z1)
    t.lt(120)
    t.fd(z3)
    t.lt(60)
    t.fd(z2)
    t.lt(60)
    t.fd(z3)
    t.end_fill()


