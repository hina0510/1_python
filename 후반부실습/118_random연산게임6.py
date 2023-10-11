# 88 문제에서 이번에는 Game out 될 경우 처리를 해볼게요.
# 만약 사용자에게 더할건지 물어보고 no 라고 하면 아예 끝내고
# 아니면 난이도 설정부터 다시 이어지도록할게요
# 그럼. 전체를 while True 싸고 사용자에게 계속할건지 물어봐야겠죠?
# 물어보는건 처음이 아니라 게임이 끝나고 break 된 다음으로 해야겠네요



import random 
import os
import time


while True:
    life = 5
    score = 0

    난이도 = int(input("난이도 하(1), 난이도 중(2), 난이도 상(3) 선택 : "))
    if 난이도 == 1:
        r1 = 1
        r2 = 9
    elif 난이도 == 2:
        r1 = 10
        r2 = 99
    else:
        r1 = 100
        r2 = 999

    while True:

   

        if life <= 0:                               # 만약 라이프가 1인데 2 가 깎이면 이부분을 처리해줘야함!!!!!!!!!!!!!!!!!!!!!!!!
            break                                     # life == 0 을 하게되면 -1이 되는순간 무한반복이됨.

        A = random.randint(r1,r2)    
        B = random.randint(r1,r2)     

        op = random.randint(0,1)        # 두 가지 케이스로 두고 0 이면 덧셈문제 출제, 1이면 뺄셈문제 출제로 설정하겠슴다
        s200 = random.randint(1,5)   # 1~5 중에 하나만 설정하면 1/5 확률이됨
        l2 = random.randint(1,4)        # 1~4 중에 하나만 설정하면 1/4 확률이됨

        print("현재 목숨 :",life,"\t현재점수 :",score)   # 문제 출력전에 현재 목숨과 점수 출력

        if s200 == 1:       # 1 이 나오면 200 점 짜리 문제라고 설정
            print("자 이문제는 200점 짜리 문제입니다.")
            점수 = 200
        else:                   # 여기서 else 를 해준이유 : 만약 200 점 문제가 출제되고 나면 계속 200점이 되는거 방지
            점수 = 100

        if l2 == 1:
            print("자 이문제는 라이프가 2개 걸린 문제입니다.")
            라이프 = 2
        else:
            라이프 = 1

        if op == 0:
            print(A,"+",B,"=",end=' ')         # 덧셈 문제를 출력하는 프로그램
            C = A + B                                  # 덧셈 문제의 정답을 저장
        elif op == 1:
            print(A,"-",B,"=",end=' ')         # 뺄셈 문제를 출력하는 프로그램
            C = A - B                                  # 뺄셈 문제의 정답을 저장

    
        user = int(input())                     # 값을 입력받고 정답과 비교해서 판단하는 부분
        if C == user:
            score += 점수
            print("맞췄습니다!!")
        else:
            life -= 라이프
            print("틀렸습니다.")

        time.sleep(1)
        os.system("cls")
    
    choice = input("계속하시겠습니까? (yes or no)")
    if choice == 'no':
        break
    # else 는 굳이 처리해주지 않아도 되겠죠? 어차피 반복 되잖아요 ㅎㅎㅎ