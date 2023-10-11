# for 은 반복횟수가 명확, while 은 반복횟수가 명확X

# for i in range(1,11):
#     print(i)

# i = 1
# while i < 11 :
#     print(i)
#     i += 1

# i = 0
# while i < 10 :
#     i += 1
#     print(i)

# i = 1
# while i < 11 :
#     print(i) # i 의 값에 변화가 없어 무한루프에 빠짐

# N = int(input("수 입력 : "))

# i = 1
# while i < 10 :
#     print(N,"X", i, "=", N*i)
#     i += 1

# i = 2
# while i < 10 :
#     j = 1
#     while j < 10 :
#         print(i,"X", j, "=", i*j)
#         j += 1
#     i += 1

# while True: (조건 볼 필요 X, 무한반복문으로 사용(나갈 때는 break))

# while True :
#     st = input("입력(stop 종료) > ")

#     if st == "stop":
#         break

# while True:
#     N =  int(input("수 입력 (종료 0): "))
#     if N == 0:
#         print("프로그램 종료")
#         break

# A = 0
# while True:
#     N =int(input("수 입력 : "))
#     if N != 0 : #li.append(N)
#         A += N
#     elif N == 0 :
#         print(A) sum(li)
#         break

# A = []
# while True : 
#     N = int(input("수 입력 : "))

#     if N == 0 :
#         print(sum(A)/len(A), "프로그램 종료")
#         break

#     A.append(N)

# while 은 사용자가 사용할 프로그램에 항상 들어있다!(에러사항을 만들지 마세요)
# 요구명세서

# 문자열.isnumeric() = 문자열이 숫자로만 구성되어 있을 때 True 

# li = []
# while True:
#     N = input("수 입력 (종료 quit) : ")

#     if N.isnumeric(): # 1) 숫자를 입력했을 때
#         li.append(int(N))
#     else: # 2) 문자를 입력했을 때
#         if N == "quit": #    2-1) 종료시그널일 때
#             print(sum(li)/len(li))
#             break
#         else:           #    2-2) 종료시그널 아닐 때
#             print("숫자 입력좀...")


# li = []
# while True :
#     W = input("python 점수 입력 (종료 : q) : ")
#     if W.isnumeric():
#         W = int(W)
#         if 0 <= W <= 100 :
#             li.append(W)
#         else :
#             print("0 ~ 100 사이의 숫자 입력")
#     else :
#         if W == "q" :
#             if len(li) > 0 :
#                 print("평균은", sum(li)/len(li))
#             else :
#                 print("입력된 점수가 없습니다")
#             break #중복 시 빼줌
#         else :
#             print("숫자 입력하세요")

# li = []
# A = 0
# while True:
#     p = input("python 점수 입력 > ")

#     if p.isnumeric(): # 1
#         p = int(p)
#         if 0 <= p <= 100: # 1-1
#             li.append(p)
#             A = 0
#         else: # 1-2
#             print("0 에서 100 까지 입력바람!!")
#             A += 1
#     else: # 2
#         if p == "quit": # 2-1
#             if li: # 2-1-1
#                 print("평균 > ", sum(li)/ len(li))
#             else: # 2-1-2
#                 print("입력된 점수가 존재하지 않습니다.")
#             break
#         else: # 2-2
#             print("숫자 입력좀...")
#             A += 1
#     if A == 3 :
#         print("입력 오류 횟수 추가")

# li1 = [300, 300, 200]
# li2 = ["콜라", "사이다", "커피"]
# M = 0
# import time
# import os

# while True:
#     print("="*10, "Menu", "="*10) 
#     print("1.", li2[0], "/ ", li1[0]) 
#     print("2.", li2[1], "/ ", li1[1]) 
#     print("3.", li2[2], "/ ", li1[2]) 
#     print("4. 돈 넣기") 
#     print("5. 잔돈 반환") 
#     print("6. 종 료") 
#     print("="*30)
#     print("현재금액 : ", M)
#     menu = int(input("메뉴 선택 : ", ))
#     print("="*30)
#     if 0 < menu < 4 : # 1. 음료 메뉴를 실행했을 때
#         if M < li1[menu-1] : #  1-1. 돈이 없거나 적을 경우
#             print("돈 넣기 메뉴를 실행하세요") #   1-1-1. "돈 넣기 메뉴를 실행하세요"
#         else : #  1-2. 돈이 있을 경우
#             print(li2[menu-1], "맛있게 드세요")
#             M-=li1[menu-1]
#     elif menu == 4 : # 2. 돈넣기 메뉴를 실행했을 때
#         A = int(input("돈을 넣어주세요 : ")) #  2-1. 돈을 넣어주세요(현재 금액에 반영)
#         M += A
#     elif menu == 5 : # 3. 잔돈반환을 실행했을 때
#         print("잔돈", M, "원이 반환됩니다") #  3-1. 잔돈이 반환됩니다(실행 후 현재 금액 리셋)
#         M = 0
#     else : # 4. 종료 실행했을 때
#         print("프로그램 종료") #  4-1. 프로그램 종료
#         for i in range(10, -1, -1):
#             print(i)
#             break
#     time.sleep(0.1)
#     os.system("cls")