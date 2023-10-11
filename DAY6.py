
# <Day6>

# 순서있는 자료형 (Subscriptable) : list 리스트[대괄호 사용], tuple 튜플(소괄호 사용), str
## index가 있음 (각각의 자료에 번호가 부여되어 있음)

# list(자료변경 가능), 튜플(자료변경 불가능)

# li = [1,2,3,4]

# li[0] = "one"

# print(li)

# # 리스트 자료형일 떄만 할 수 있어요
# li = [1,"hello"]

# # 1. 맨 뒤에 자료추가
# # 리스트.append(x) x가 맨 뒤에 추가
# li.append(1.2)
# print(li)
# li.append(True)
# print(li)

# # 2. 원하는 위치에 자료추가
# # 리스트.insert(idx, x) # idx 위치에 X 추가 
# li.insert(0, 'world') # 0번 인덱스에 'world' 추가
# print(li)

# # 3. 원하는 위치에 자료제거 및 반환
# # 리스트.pop(index) #index 위치에 자료를 제거 (idx 디폴트 맨 뒤)
# x = li.pop(2)
# print(x, "가 제거된 리스트", li)

# # 4. 원하는 자료와 인덱스 반환
# x = li.index(1.2)
# print(x)

# # 5. 자료 개수를 반환
# # 리스트.count(x)
# li = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# x = li.count(1)
# print(1, "은", x, "개 들어있다.")

# words = ['apple', 'banana', 'air']
# print(words)
# user = input("삭제할 단어를 입력해주세요 : ")

# if words.count(user): # 자료 개수 반환
#     idx = words.index(user) # 인덱스 반환
#     words.pop(idx) # 제거
# else :
#     print("그런 단어 없음")
# print(words)

# 6. 리스트 정렬
# 리스트.sort()  # 단, 리스트 내의 자료형 일치
# li1 = [3.4, 2, 10, 1, 3, 6, 1.2, 19]
# li1.sort()
# print(li1)
# 문자열도 정렬가능

# 7. 리스트 뒤집기
# 리스트.reverse()
# li1.reverse()
# print(li1)

# 8. 리스트 비우기
# 리스트.clear()
# li1.clear()
# print(li1)

# li = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]

# 리스트 사용 시 유용한 표현 len, sum 함수
# len(리스트) > 자료의 개수 반환
# sum(리스트) > 자료의 합 반환

# print(len(li))
# print(sum(li))
# print(sum(li)/len(li))

# iterable (반복가능한) 자료형 :str, list, tuple, set, dict
# for [반복문에서 사용될 변수] in [iterable 자료형]

# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(i)

# li = [1, True, "hello", 3.4, "world", 3-2j]
# for i in li:
#     print(i)

# range([start:0], stop, [step:1])   stop-1까지 리스트 작성   [] 생략가능
# (1가지): stop / (2가지):start, stop / (3가지):start, stop, step

# range(22)
# range(41,53)
# range(10,1000)

# for i in range(1,1001):
#     print(i)

# N = int(input("수 입력 : "))
# for i in range(1, N+1):
#     print(i)

# N = int(input("수 입력 : "))
# for i in range(N, 0,-1):
#     print(i)

# A = int(input("수 입력 : "))
# B = int(input("수 입력 : "))

# if A < B :
#     for i in range(A+1, B):
#         print(i)
# elif A > B  : 
#     for i in range(A-1, B, -1):
#         print(i)

# 복합연산자 주의사항 : 기존에 변수가 세팅되어있어야함

# su = 0
# for i in [1,2,3,4]:
#     su += i
# print(su)

# su = 0
# N = int(input("수 입력 : "))
# for i in range(1, N+1):
#     su += i
# print(su)

# su = 1
# N = int(input("수 입력 : "))
# for i in range(1, N+1):
#     su *= i
# print(su)

# 1에서 10까지 홀수, 짝수 판별
# for i in range(1,11):
#     if i % 2 == 0 :
#         print("짝수")
#     else : 
#         print("홀수")

# N = int(input("수 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0 :
#         print(i, "짝수")

# even = 0
# odd = 0
# N = int(input("수 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0 :
#         even += i #(1 대입하면 갯수)
#     else :
#         odd += i
# print(even,odd)

# even = []
# odd = []
# N = int(input("수 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0 :
#         even.append(i) 
#     else :
#         odd.append(i)
# print(even,odd)
# print(sum(even), sum(odd))
# print(len(even), len(odd))

# S = 0
# C = 0
# N = int(input("수 입력 : "))
# for i in range(1,N+1):
#     if i % 7 == 0 :
#         S +=i
#         C +=1
# print(S, C)

# S = []
# N = int(input("수 입력 : "))
# for i in range(1,N+1):
#     if i % 7 == 0 :
#         S.append(i)
# print(sum(S), len(S))

# N = int(input("수 입력 : "))
# li = []
# for i in range(1,N+1) : 
#     if i % 7 == 0 :
#         li.append(i)
#         print(li)

# print(li) ~나서 = [7,14]
#     print(li) ~때 마다(조건문 : 실행의 유무) = [], [], [], [], [], [], [7], [7], [7], [7], [7], [7], [7], [7,14] ,[7,14]  
#         print(li)  ~면서(반복문 : 반복횟수) = [7], [7,14]

# li = ["D", "A", "B", "C"]
# for i in range (20,51) :
#     print(i, li[i%4])

# A = int(input("수 입력 : "))
# B = int(input("수 입력 : "))

# if A > B :
# for i in range(B+1, A) :
#     if i % 2 == 0 :
#         print(i, end="")

# S = 0
# C = 0
# N = int(input("수 입력 : "))

# for i in range(1,N+1):
#     if i % 7 == 0 :
#         S += i
#         C += 1
# print(S, C)

# A = 0
# B = 0
# N = int(input("수 입력 : "))

# for i in range(1,N+1):
#     if i % 3 == 0:
#         A += 1
#     if i % 5 == 0:
#         B += 1

# if A > B :
#     print(A-B)
# else :
#     print(B-A)

# li = ['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A', 'A', 'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']
# for i in ["A", "B", "AB", "O"] :
#     print(i, li.count(i), 명)

# A = 0
# B = 0
# O = 0
# AB = 0
# for i in li :
#     if i == "O" :
#         O += 1
#     elif i == "A":
#         A += 1
#     elif i == "B":
#         B += 1
#     else :
#         AB += 1
# print("A형 : ", A, "명,", "B형 : ", B, "명,", "O형 : ", O, "명,","AB형 : ", AB, "명,")

# li = [6600, 4800, 3400, 3200, 4500, 5500, 3200, 7800, 4200, 5300, 7500, 4200, 7200, 5600, 6700, 8000, 7000, 6700, 6200, 6100, 4700, 7200, 7100, 5700, 5900, 4300, 5200, 5600, 5900, 6600, 4900, 5800, 7100, 5800, 4500, 3200, 7800, 5300, 7200, 8000]
# M = 0
# for i in li:
#     if i <= 5000 :
#         M += 1
# print(M, "개")

# li = [80, 70, 44, 66, 40, 80, 77, 57, 68, 90, 75, 84, 99, 52, 45, 53, 54, 96, 59, 47, 57, 68, 74, 68, 79, 60, 63, 67, 43, 100, 43, 54, 77, 59, 75, 60, 97, 47, 100, 54]
# C = 0
# for i in li :
#     if i <80 :
#         C += 1
# print(C, "명")

# M = int(input("단 입력 : "))
# for i in range(1,10):
#     A = M * i
#     print(M, "X", i, "=", A)

# A = int(input("몇 회 연산을 진행하시겠습니까? : "))

# for i in range(A)

# B = int(input("수 입력 : "))
# C = int(input("수 입력 : "))
# print("="*30)
# print("1. 더하기")
# print("2. 빼기")
# print("3. 곱하기")
# print("="*30)

# if A == 1 :
#     print(B, "+", C, "=", B+C)
# elif A == 2 :
#     print(B, "-", C, "=", B-C)
# elif A == 3 :
#     print(B, "*", C, "=", B*C)
# else :
#     print("그런 연산 없습니다")


# Y = 0
# for i in range(2000, 3001) :
#     if i % 400 == 0 : 
#         Y += 1 # = li.append(i)
#     elif i % 400 == 0 :
#         Y += 1 # = li.append(i)
#     elif i % 100 == 0 :
#         pass

#     if Y ==135 :
#         print(i) #print(li[134])

# print("윤년 : ", Y, "번")

# A = int(input("몇 회 입력하시겠습니까? : "))

# for i in range(A):

#     B = int(input("수 입력 : "))

#     if B % 2 == 0 :
#         print(B,"짝수")
#     else :
#         print(B,"홀수")

# A = int(input("몇 회 입력하시겠습니까? : "))
# li = []
# for i in range(A):
#     B = int(input("수 입력 : "))
#     li. append(B)

# for i in li :
#     if i % 2 == 0 :
#         print(i, "짝수")
#     else :
#         print(i, "홀수")

# S = int(input("학생은 몇 명 인가요? : "))
# li = []
# P = 0
# B = 0
# for i in range(S) : 
#     T = int(input("점수 입력 : "))
#     li.append(T)

# for i in li :
#     P += i
#     A = P/S
    
# print(S, "명의 평균", A)

# for i in li :
#     if i <= A :
#         B += 1
# print("평균 이하인 학생", B, "명")

# A = int((input("수 입력 : ")))
# li = []
# B = 0
# C = ""
# for i in range(1,A+1):
#     li.append(i)

# for i in li :
#     C += str(i)
#     B = len(C)

# print(C, ">", B)
