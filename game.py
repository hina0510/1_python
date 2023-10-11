import random


A = random.randint(1,4)
B = random.randint(1,13)

for i in A :
    if i == 1 :
        A = "♥"
    elif i == 2 :
        A = "◆"
    elif i == 3 :
        A = "♠"
    else :
        A = "♣"

if B == 1 :
    B = ("A", 1)
elif B == 11 :
    B = ("J", 11)
elif B == 12 :
    B = ("Q", 12)
elif B == 13 : 
    B = ("K", 13)

com = print(A, B)

user = []
print(A, B) # 1. 카드 1장 나눠줌

while True :
    print("카드 추가 / hit ")
    print("멈추기 / stop ") 
    S = input("hit or stop :")
    if S == 'hit': #  1-1. hit (카드 1장 추가)
        C = user, (A, B)
        print(C)
        user.append(A, B)
    elif S == 'stop' : #  1-2. stop (멈추기)
        pass
        
    else :
        print("다시 입력하세요")



 
#   1-2-1. 수 합하기
#   1-2-2. com user 수 비교
#   1-2-3. 승패
#    1-2-3-1. 이겼을 때
#     1-2-3-1-1. WIN!!
#    1-2-3-2. 졌을 때
#     1-2-3-2-1. LOSE!!









