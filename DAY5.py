# <Day5>

# elif = else if. if(시작) > elif > else(끝) 순서로 사용

# if choice == 1:
#     print("1번 선택")
# elif choice == 2:
#     print("2번 선택")
# elif choice == 3:
#     print("3번 선택")
# elif choice == 4:
#     print("4번 선택")
# else :
#     print("해당 없음")


# 조건의 유무(if, elif O , else X)

# A = int(input("수를 입력 : "))

# if A > 0 :
#     print("양수")
# elif A < 0 : 
#     print ("음수")
# else :
#     print ("0")

# A = int(input("수 입력 : "))

# if A % 2 == 0 :
#     print("짝수")
# else :
#     print("홀수")

# M = int(input("수학 성적 : "))
# S = int(input("과학 성적 : "))

# A = (M + S)/2

# if A >= 90 :
#     print("A")
# elif A >= 80 :
#     print("B")
# elif A >= 70 :
#     print("C")
# else :
#     print("D")

# A = int(input("수 : "))
# B = int(input("수 : "))
# C = input("연산자 : ")

# if C == "+" :
#     print(A, "+", B, "=", A+B)
# elif C == "-" :
#     print(A, "-", B, "=", A-B)
# elif C == "*" :
#     print(A, "*", B, "=", A*B)
# elif C == "//" :
#     print(A, " //", B, "=", A//B)
# else :
#     print("연산자가 이상해요.")

# 아이디 = input("아이디 입력 : ")

# if 아이디 == "admin" :
#     패스워드 = input("패스워드 입력 : ")
#     if 패스워드 == "admin" :
#         print("LOGIN SUCCESS")
#     else :
#         print("WRONG PASSWORD")
# else : 
#     print("NO USER...")

# A = int(input("수 입력 : "))

# if A >= 0 :
#     print("절대값은",  A, "입니다.")
# else :
#     print("절대값은",  -A, "입니다.")

# AP = 3000
# BP = 2000

# print("="*30)
# print("사과 : ", AP)
# print("배 : ", BP)
# print("="*30)

# A = int(input("사과의 수 : "))
# B = int(input("배의 수 : "))
# M = int(input("소지 금액 : "))

# T = A * AP + B * BP

# if T <= M : 
#     print("잔 돈 : ", M - T)
# else :
#     print("구매불가", T, "원이 필요합니다.")

# M = int(input("월 입력 : "))

# if M == 1 or M == 2 or M == 12: /가을 뒤에 1 <= M <= 12
#     print("겨울")
# elif 3 <= M <= 5 :
#     print("봄")
# elif 6 <= M <= 8 :
#     print("여름")
# elif 9 <= M <= 11 :
#     print("가을")
# else :
#     print("입력이 바르지 않습니다.")

## 유효성 검사 먼저 (pass)
# if 1 <= M <= 12 : 
#     pass
# else : 
#     print("입력오류")
# if 1 <= M <= 12 :
#     if 3 <= M <= 5 :
#     print("봄")
#     elif 6 <= M <= 8 :
#     print("여름")
#     elif 9 <= M <= 11 :
#     print("가을")
#     else :
#         print("겨울")
# else :
#     print("입력이 바르지 않습니다.")

# A = int(input("수 입력 : "))

# if A % 15 == 0 :
#     print("15의 배수 입니다.")
# elif A % 3 == 0 :
#     print("3의 배수 입니다.")
# elif A % 5 == 0 : 
#     print("5의 배수 입니다.")

# print("="*30)
# print("1. 아메리카노")
# print("2. 카페라떼")
# print("="*30)
# M = (int(input("메뉴 선택 : ")))
# print("="*30)
# print("1. ICE")
# print("2. HOT")
# print("="*30)
# C = (int(input("온도 선택 : ")))

# if M == 1 :
#     if C == 1 :
#         print("아이스 아메리카노 선택")
#     elif C == 2 :
#         print("아메리카노 선택")
    
# elif M == 2 :
#     if C == 1 :
#         print("아이스 카페라떼 선택")
#     elif C == 2 :
#         print("카페라떼 선택")

# Y = int(input("생년월일 : "))

# B = Y % 12

# if B == 0 : 
#     print("원숭이")
# elif B == 1 : 
#     print("닭")
# elif B == 2 : 
#     print("개")
# elif B == 3 : 
#     print("돼지")
# elif B == 4 : 
#     print("쥐")
# elif B == 5 : 
#     print("소")
# elif B == 6 : 
#     print("호랑이")
# elif B == 7 : 
#     print("토끼")
# elif B == 8 : 
#     print("용")
# elif B == 9 : 
#     print("뱀")
# elif B == 10 : 
#     print("말")
# else : 
#     print("양")

# D = int(input("일 : "))
# T = D % 4

# if T == 0 : 
#     print("D")
# elif T == 1 : 
#     print("A")
# elif T == 2 : 
#     print("B")
# else :
#     print("C")

# print("오늘 : 화요일")
# D = int(input("일 수 : "))
# T = D % 7

# if T == 0 :
#     print("화요일")
# elif T == 1 :
#     print("수요일")
# elif T == 2 :
#     print("목요일")
# elif T == 3 :
#     print("금요일")
# elif T == 4 :
#     print("토요일")
# elif T == 5 :
#     print("일요일")
# else :
#     print("월요일")

# Y = int(input("연도 : "))

# if Y % 4 == 0 :
#     if Y % 400 == 0 :
#         print("윤년")
#     elif Y % 100 == 0 :
#         print("평년")
#     else :
#         print("윤년")
# else :
#     print("평년")

# T = int(input("몇 번째 역 : "))
# S = T % 8

# if S == 0 :
#     print("A")
# elif S == 1 or S == 7:
#     print("B")
# elif S == 2 or S == 6:
#     print("C")
# elif S == 3 or S == 5:
#     print("D")
# else :
#     print("E")

# H = int(input("시 : "))
# M = int(input("분 : "))

# if M >= 30 :
#     print(H, "시", M-30, "분")
# else :
#     print(H-1, "시", M+30, "분")

# A = int(input("세자리수 입력 : "))
# B = int(input("세자리수 입력 : "))

# AT = A % 10 * 100 + A // 10 % 10 * 10 + A // 100
# BT = B % 10 * 100 + B // 10 % 10 * 10 + B // 100

# if AT > BT : 
#     print(AT)
# elif AT < BT :
#     print(BT)
