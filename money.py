m = int (input("투입한 돈 :"))
p = int (input("물건값 :"))
change = m - p
coin500s = change//500
coin100s = (change%500)//100
print("거스름돈 : ",change)
print("500원 동전의 개수 : ",coin500s)
print("100원 동전의 개수 : ",coin100s)
