# <Day3>
# input(문자열) enter전까지 입력가능
# print(input("입력 : ")) 안쪽부터 함수 적용

# x = input("입력 : ") 입력된 자료를 x변수에 대입
# x = input("입력 : ")
# print(x, "가 입력됨!")

# name = input("이름 : ")
# age = input("나이 : ")
# email = input("이메일 : ")
# print("이름", name)
# print("나이", age)
# print("이메일", email)

# x = int(input("x = "))
# y = int(input("y = "))

# print(x, "+", y, "=", x+y)
# print(x, "-", y, "=", x-y)
# print(x, "*", y, "=", x*y)
# 반환값은 무조건 문자열
# x = int(input("x = ")) or x = input("x = ") x = int(x)
# y = int(input("y = ")) or y = input("y = ") y = int(y)

# kor = int(input("국어점수 : "))
# math = int(input("수학점수 : "))
# sci = int(input("과학점수 : "))

# avg = (kor+math+sci)/3
# avg = round(avg, 2)
# print("평균 : ", avg) 
# 식을 변수로 바꾸면 변수만 바꿔주면 편함(변동이 잦을 것 같은 값>변수로 처리!)

# AP = 3000
# BP = 2000

# print("="*30)
# print("사과 / ", AP)
# print("배 / ", BP)
# print("="*30)

# A = int(input("사과 : "))
# B = int(input("배 : "))

# T = A*AP+B*BP
# print("총 금액 : ", T)

# H = int(input("시 : "))
# M = int(input("분 : "))
# S = int(input("초 : "))

# HS = H*3600
# MS = M*60
# T = int(HS+MS+S)

# print("총 초수 ", T)

# S = float(input("섭씨 온도 : "))
# F = S*1.8+32

# print("섭씨 온도는", S, "도, ", "화씨 온도는", F, "도, ")

# print("="*30)
# print("책책책 책을 읽읍시다")
# print("="*30)

# TP = float(input("전체 페이지 수 : "))
# NP = float(input("현재 페이지 수 : "))
# T = round((NP/TP*100),2)
# print(T, "%")

# print("="*30)
# print("한라산 정상까지 얼마나 남았을까")
# print("="*30)

# NM = int(input("현재 높이 (m) : "))
# T = round((1947-NM)/1947*100, 2)

# print("앞으로", T, "% 더 올라가야해요!!")

# a = 728
# X = a//100
# Y = a//10%10
# Z = a%10
# print("입력 : 728")
# print("백의자리는", X, "십의자리는", Y, "일의자리는", Z, "입니다.")

# print("="*30)
# print("생년월일을 구하시오.")
# print("="*30)

# B = 19870511
# Y = B//10000
# M = B//100%100
# D = B%100

# print(Y, "년", M, "월", D, "일 생")

# TS = int(input("초 : "))
# H = TS//3600
# M = TS//60%60
# S = TS%60

# print(H,"시간", M,"분", S, "초")