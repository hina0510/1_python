# time.sleep(x) = x초간 코드 실행 멈춤
# T = time.time() > 상대 시간
# time.time() - T > 경과 시간
# os.system("cls") = 화면을 지워줌

# import time
# import os

# for i in range(1,101):
#     print(i)
#     time.sleep(0.1)
#     os.system("cls")

# import random

# for i in range(100):
#     print(random.randint(1,10))

# # A 부터 B 까지 랜덤 수 반환!!

# import random
# import time
# import os

# # 홀짝
# life = 5
# score = 0

# while True :
#     print("="*30)
#     print("1. 홀수")
#     print("2. 짝수")
#     print("♥"*life + "♡*(5-life)")
#     print("="*30)
#     com = random.randint(1,10)
#     user = int(input("선택>"))

#     if com % 2 == user % 2 :
#         print("맞았습니다")
#         score += 100
#     else :
#         print("틀렸습니다")
#         life -= 1

#     if life == 0 :
#         print("니 점수", score)
#         break

#     time.sleep(0.7)
#     os.system("cls")


# com = random.randint(1,10)

# user = input("홀?짝?")

# if com % 2 == 0 :
#     if user == "짝":
#         print("맞았습니다")
#     else :
#         print("틀렸습니다")
# else :
#     if user == "홀":
#         print("맞았습니다")
#     else :
#         print("틀렸습니다")
# print("랜덤 수  :", com)

# 업다운 게임

# import random
# import time
# import os

# A = 0
# L = 0
# print("="*30)
# print("1. EASY(한자리)")
# print("2. NORMAL(두자리)")
# print("3. HARD(세자리)")
# print("="*30)

# L = int(input("난이도 (번호입력): "))
# if L == 1 :
#     com = random.randint(1,9)
# elif L == 2 :
#     com = random.randint(10,99)
# elif L == 3 :
#     com = random.randint(100,999)
# else : 
#     print("없는 난이도입니다")

# while True :
#     print("시도 횟수 : ", A)
#     user = int(input("수 입력 : ")) # 1. 사용자가 수를 입력
#     print("="*30)
#     A += 1
#     if user > com : #  1-1. 지정된 수보다 클 때
#         print("DOWN!") #   1-1-1. DOWN!
        
#     elif user < com : #  1-2. 지정된 수보다 작을 때
#         print("UP!") #   1-2-1. UP!
#     else : #  1-3. 지정된 수와 같을 때
#         print("Correct!") #   1-3-1. Correct!
#         print("시도 횟수 : ", A)
#         break
    
# else : # 2. 사용자가 범위 외의 수를 입력
#     print("수를 다시 입력하세요") # 2-1. 수를 다시 입력하세요

# time.sleep(1.5)
# os.system("cls")

# import random
# import time

# print("="*30)
# print("1. EASY")
# print("2. NORM")
# print("3. HARD")
# print("="*30)
# level = int(input("난이도 입력 > "))

# if level == 1:
#     mi = 1
#     ma = 9
# elif level == 2:
#     mi = 10
#     ma = 99
# elif level == 3:
#     mi = 100
#     ma = 999

# t = time.time()

# com = random.randint(mi, ma) # 변수 지정(최소, 최대)
# cnt = 0

# while True:
#     print(mi, ma)
#     user = int(input("수 입력 > "))
#     cnt += 1

    
#     if mi <= user <= ma: # 유효한 범위일때
#         if user > com:
#             print("DOWN!")
#             ma = user - 1 # 입력값이 랜덤 수 보다 커서 입력값-1(범위 좁힘)
#         elif com > user:
#             print("UP!")
#             mi = user + 1 # 입력값이 랜덤 수 보다 작아서 입력값+1(범위 좁힘)
#         else:
#             print("CORRECT!!")
#             clear = round(time.time()-t, 2)
#             print(clear, "초 걸림", cnt, "번 만에 맞춤")
#             break
#     else:
#         cnt += 2
#         print("패널티 적용!! 1초간 Freeze")
#         time.sleep(1)

# 연산 결과를 맞추는 게임

# import random

# life = 5
# score = 0

# while True:
    
#     print("="*30)
#     print("★ "*life + "☆ "*(5-life))
#     print("점수 : ", score)
#     print("="*30)

#     A = random.randint(1,9)
#     B = random.randint(1,9)
#     C = random.randint(1,2)
#     Q = random.randint(1,5)
#     M = random.randint(1,10)

#     if Q == 1 :
#         점수 = 200
#         print("이번 문제는 200점!")
#     else :
#         점수 = 100
    
#     if M == 1 :
#         별 = 2
#         print("이번 문제는 못맞추면 -2!")
#     else :
#         별 = 1
    
#     if C == 1 :
#         print(A, "+", B, "=", end=" ")
#         D = A+B
#     else :
#         print(A, "-", B, "=", end=" ")
#         D = A-B

#     user = int(input())

#     if user == D :
#         print("맞았습니다")
#         score += 점수
#     else :
#         print("틀렸습니다")
#         life -= 별

#     if life == 0 :
#         print("점수 : ", score)
#         break

# str, list, tuple => index를 가짐

# B =[]
# err = 0
# print("START!")
# W = input("시작단어를 입력하세요 : ")

# while True :
#     print(W ,":", end = " ")
#     A = input()
#     if W[-1] == A[0]:
#         if A in B :
#             err +=1
#             if err == 2 :
#                 print("게임오버!")
#                 break
#         print("PASS!:)")
#         W = A
#         B.append(A)
#     else :
#         print("FAIL!:(")
#         break

