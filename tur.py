# 파이썬 셀에서 left를 의미하는 "1"를 입력하면 거북이가 왼쪽으로 100픽셀 이동하고
# right를 의미하는 "r"를 입력하면 거북이가 오른쪽으로 100픽셀 이동하는 프로그램
#
# 해결 방법 : 터틀을 import해 명령어를 각각 'r'과 '1'에
# 입력하고 for문을 사용하여 사용자가 여러번 사용할 수 있게 한다.

import turtle
t = turtle.Turtle() # t 에 turtle.Turtle 치환
t.shape("turtle") # 거북이 모양으로 변환
t.shapesize(3,3) # 거북이의 크기 3배 늘림
for i in range(0,10): # for문 사용 10번 반복
    a = input("명령을 입력하시오: ") # 'a'에 사용자 입력 받기
    if a =='1': # 'a'가 '1'일 경우 왼쪽으로 90도 돌고 100픽셀 이동
        t.left(90)
        t.forward(100)
    elif a =='r': # 'a'가 'r'일 경우 오른쪽으로 90도 돌고 100픽셀 이동
        t.right(90)
        t.forward(100)
t.exitonclick()