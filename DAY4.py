
# <Day4>

# True, False 첫 글자는 대문자로
# 숫자 0과 문자열 ''은 False (공백은 True)

# a = 10 # 대입

# print(a>0)
# print(a<3)
# print(a==1) # 같다
# print(a!=2) # 다르다
# print(a>=4) # 한번에 비교 가능(1<=a<=10)
# print(a<=5)

# b = "hello"  #문자열끼리 비교 전부 가능
# b == "hello"
# b != "hello" #False

# 문자열과 숫자 비교(부등호 사용 시 에러) ==, !=

# "1"==1
# "1"!=1
# "1">1

# True and True
# True or True
# True or False
# False or True  일 때 True

# 연산자 우선순위 (산술>비교>논리)
# */ > +- > == > and > or > (not)

# a = 7

# a % 3 == 1 or 0 < a < 7 and a // 3 >= 2
# 1 == 1 or 0 < 7 < 7 and 2 >= 2
# True or False and True
# True

# = 은 다음 문장은 무조건 종속 문장이 나온다.
# 종속문장은 칸을 띄워주어야 함. 라인을 맞춰줘야 함.(Tab 1번 or Space 4번)

# A = int(input("수 입력 : "))

# if 10 <= A < 100 : # 두 자리수 일 때
#     print("두 자리수 입력!")

# A = int(input("수 입력 : "))

# if a > 0 : 
#     print("양수 입력")
# if a < 0 : 
#      print("음수 입력")
# if a == 0 : 
#       print("0 입력")

# A = int(input("수 입력 1 : "))
# B = int(input("수 입력 2 : "))

# if A > B :
#     print(A)
# if A < B :
#     print(B)
# if A == B :
#     print("같다.")

# A = int(input("수 입력 : "))

# if A % 2 == 0 :
#     print(A, "짝수")
# if A % 2 == 1 :
#     print(A, "홀수")

# A = int(input("수 입력 : "))

# if A % 7 == 0 : 
#     print(A, "7의 배수다")
# if A % 7 != 0 : 
#     print(A, "7의 배수가 아니다")

# K = int(input("국어 점수 : "))
# M = int(input("수학 점수 : "))

# A = ( K + M )/2

# if A >= 80 :
#     print("합격")
# if A < 80 :
#     print("불합격")

# A = int(input("두 자리수 입력 : "))
# B = int(input("두 자리수 입력 : "))

# C = A % 10 + B % 10

# if C >= 10 : 
#     print("올림이다")
# if C < 10 : 
#     print("올림이 아니다")

# C = (A + B)//10
# D = A // 10 + B // 10

# if C > D : 
#     print("올림이다")
# if C == D : 
#     print("올림이 아니다")

# A = int(input("수를 입력하세요 : "))
# B = int(input("수를 입력하세요 : "))
# C = (input("연산을 입력하세요 : "))

# if C == "+" : 
#     print( A, "와 ", B, "의 합은 ", A + B)
# if C == "-" : 
#     print( A, "와 ", B, "의 차는 ", A - B)
# if C == "*" or "x" or "X" : 
#     # == 을 우선 계산 <= 각각 나눠줌(C == "*" or C == "x" or C == "X" )
#     print( A, "와 ", B, "의 곱은 ", A * B)
# if C == "//" or "/": 
#     print( A, "와 ", B, "의 나누기는 ", A // B)
