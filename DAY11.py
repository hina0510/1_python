# replace 는 앞의 문자열에서 A 를 B로 바꾼 결과를 반환할 뿐 a 자체를 바꾸진 않는다

# a = "apple"
# print(a.replace("p", "t"))
# print(a)

# A = input("문구를 입력하세요 : ")

# while True :
#     W = input("가릴 문자 입력 (입력완료 quit) : ")
#     if W == "quit" : 
#         print(A)
#         break
#     else :
#         A = A.replace(W, "*")

# 파일이름으로 사용할 수 없는 문자 덜어내기
# \ " / < > | ? : *

# A = input("파일이름 입력 : ")

# for i in "\\\"/<>|?:*" :
#     A = A.replace(i, "")
# print(A)

# 문자열.count("A") A랑 같은 문자의 개수
# 문자열.split().count("A") list.count 일치 여부 확인

# A = 0

# for i in range(1,1235):
#    A += str(i).count("2")
# print(A)

# li = """my life is  been magic  seems fantastic
# i used to have a hole in the wall with a mattress
# funny when you want it  suddenly you have it
# you find out that your gold is  just plastic
# every day  every night
# i have  been thinking back on you and i
# every day  every night
# i worked my whole life
# just to get right  just to be like
# look at me  i am  never coming down
# i worked my whole life
# just to get high  just to realize
# everything i need is on the
# everything i need is on the ground
# on the ground
# everything i need is on the ground
# nah  but they do not  hear me though
# yeah  what goes up must come down
# nah  but they do not  hear me though
# you are  running out of time
# my world is  been hectic  seems electric
# but i have  been waking up with your voice in my head
# and i am  tryna send a message and let you know that
# every single minute i am  without you  i regret it
# every day  every night
# i have  been thinking back on you and i
# every day  every night
# i worked my whole life
# just to get right  just to be like
# look at me  i am  never coming down
# i worked my whole life
# just to get high  just to realize
# everything i need is on the
# everything i need is on the ground
# on the ground
# everything i need is on the ground
# nah  but they do not  hear me though
# yeah  what goes up must come down
# nah  but they do not  hear me though
# you are  running out of time
# i am  way up in the clouds
# and they say i have  made it now
# but i figured it out
# everything i need is on the ground  yeah  yeah
# just drove by your house  just drove by your house
# so far from you now  so far from you now
# but i figured it out
# everything i need is on the
# everything i need is on the ground
# on the ground
# everything i need is on the ground
# nah  but they do not  hear me though
# on the ground
# nah  but they do not  hear me though
# everything i need is on the ground"""

# W = li.split()
# for i in W :
#     if W.count(i) == 1 :
#         print(i)

# X = int(input("몇 번째 박수? : ")) # 1. 숫자 입력 몇번째 박수인가?
# A = 0
# B = 1
# while True :
#     for i in "369" : #  1-1. 1~A 까지의 숫자에 3,6,9 가 포함 될 때 박수
#         A += str(B).count(i)         #   1-1-1. 박수 칠 때마다 카운트
#     if X <= A :     #    1-1-1-1. X 가 입력한 횟수와 일치할 때 
#         break
#     B += 1
# print(B) #     1-1-1-1-1. 프린트 X번째 박수는 N

# N = int(input(수 입력 : ))
# st = ""
# num = 1
# while True : 
#     st += str(num)

#     if st.count(str(N)) >= N :
#         break
#     num += 1

# print(num)

# 문자열.strip() 공백 제거(중간은 X)
# 문자열.upper() 대문자로 바꿈
# 문자열.lower() 소문자로 바꿈

# A = input("문장입력 : ")

# print(A[0].upper()+A[1:].lower())

# ord(문자) = 문자의 숫자화
# chr(숫자) = 숫자의 문자화

# li = """50668 47084 48516 32 54252 44592 54616 51648 32 47560 49464 50836 32 54624 32 49688 32 51080 50612 50836 126 126 32 112 121 116 104 111 110 32 50640 49436 32 47928 51228 32 51217 44540 54616 45716 32 49324 44256 47141 51012 32 44592 47476 49884 44256 32 45796 47480 32 44284 47785 50640 49436 32 51312 44552 51060 45208 47560 32 49688 50900 54616 44172 32 54617 49845 54616 49492 50556 32 54633 45768 45796 33 33 33 32 51109 45812 54616 45716 45936 32 47928 51228 45716 32 51228 32 49688 50629 32 46412 32 54396 44172 32 45908 32 50612 47140 50872 32 44144 50640 50836"""

# for i in li.split():
#     print(chr(int(i)), end="")

# A = input("문자 입력 : ")

# for i in A :
#     print(ord(i), end = " ")

# A ~ Z > 65 ~ 90
# a ~ z > 97 ~ 122

# import random

# for i in range(100):
#     print(chr(random.randint(97,122)))

# N = int(input("수 입력 : "))
# su = 0
# for i in range(2,10) :
#     for j in range(1,10) :
#         print(i, "X", j, "=", i*j)
# st = """2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
# 3 X 4 = 12
# 3 X 5 = 15
# 3 X 6 = 18
# 3 X 7 = 21
# 3 X 8 = 24
# 3 X 9 = 27
# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 6 X 1 = 6
# 6 X 2 = 12
# 6 X 3 = 18
# 6 X 4 = 24
# 6 X 5 = 30
# 6 X 6 = 36
# 6 X 7 = 42
# 6 X 8 = 48
# 6 X 9 = 54
# 7 X 1 = 7
# 7 X 2 = 14
# 7 X 3 = 21
# 7 X 4 = 28
# 7 X 5 = 35
# 7 X 6 = 42
# 7 X 7 = 49
# 7 X 8 = 56
# 7 X 9 = 63
# 8 X 1 = 8
# 8 X 2 = 16
# 8 X 3 = 24
# 8 X 4 = 32
# 8 X 5 = 40
# 8 X 6 = 48
# 8 X 7 = 56
# 8 X 8 = 64
# 8 X 9 = 72
# 9 X 1 = 9
# 9 X 2 = 18
# 9 X 3 = 27
# 9 X 4 = 36
# 9 X 5 = 45
# 9 X 6 = 54
# 9 X 7 = 63
# 9 X 8 = 72
# 9 X 9 = 81"""
# a= ""
# for i in "3579":
#     a += str(st.count(i))
# print(a)
#         if str(i*j).count(i) == N :
#             su += 1
# print(su)

# li = """54620 45804 46041 50504 32 44256 49373 47566 51004 49512 49845 45768 45796 126 32 54056 49828 50892 46300 45716 32 52264 47049 32 48264 54840 54032 50640 32 51080 45716 32 49707 51088 47484 32 52264 47168 45824 47196 32 51077 47141 54616 49884 47732 32 46121 45768 45796 46 32 50937 32 48652 46972 50864 51200 32 50668 49884 44256 33 33 32 50668 44592 47196 32 46308 50612 44032 48372 49464 50836 32 104 116 116 112 115 58 47 47 119 119 119 46 99 111 117 112 97 110 103 46 99 111 109 47 118 112 47 112 114 111 100 117 99 116 115 47 53 49 50 51 50 54 56 49 48 49 63 105 116 101 109 73 100 61 55 48 48 53 48 48 57 53 48 51 38 118 101 110 100 111 114 73 116 101 109 73 100 61 55 52 50 57 55 50 55 51 57 52 50 38 115 114 99 61 49 48 52 50 53 48 51 38 115 112 101 99 61 55 48 51 48 52 55 55 55 38 97 100 100 116 97 103 61 52 48 48 38 99 116 97 103 61 53 49 50 51 50 54 56 49 48 49 38 108 112 116 97 103 61 73 55 48 48 53 48 48 57 53 48 51 86 55 52 50 57 55 50 55 51 57 52 50 65 51 52 51 53 50 51 54 53 51 38 105 116 105 109 101 61 50 48 50 50 49 50 51 48 49 52 53 56 52 56 38 112 97 103 101 84 121 112 101 61 80 82 79 68 85 67 84 38 112 97 103 101 86 97 108 117 101 61 53 49 50 51 50 54 56 49 48 49 38 119 80 99 105 100 61 49 54 55 49 48 55 56 53 54 55 55 52 57 49 48 48 53 52 57 53 51 49 49 38 119 82 101 102 61 38 119 84 105 109 101 61 50 48 50 50 49 50 51 48 49 52 53 56 52 56 38 114 101 100 105 114 101 99 116 61 108 97 110 100 105 110 103 38 65 100 78 111 100 101 73 100 61 51 52 51 53 50 51 54 53 51 38 103 99 108 105 100 61 69 65 73 97 73 81 111 98 67 104 77 73 95 99 51 99 113 116 83 103 95 65 73 86 66 115 69 87 66 82 51 56 104 119 67 101 69 65 81 89 65 105 65 66 69 103 73 89 66 102 68 95 66 119 69 38 99 97 109 112 97 105 103 110 105 100 61 49 57 48 55 51 50 49 53 51 53 57 38 97 100 103 114 111 117 112 105 100 61 49 52 55 53 51 52 52 48 55 52 48 49 38 105 115 65 100 100 101 100 67 97 114 116 61"""

# for i in li.split():
#     print(chr(int(i)), end = "")

# 문자열 포맷팅
# for i in range(2,10):
#     for j in range(1,10):
#         # 1. 서식문자 표기법 . 정수 %d , 실수 %f , 문자열 %s
#         print("%d x %d = %d" % (i,j,i*j))

#         # 2. format 이라는 문자열 함수 {}
#         print("{} x {} = {}".format(i,j,i*j))

#         # 3. f string!!
#         print(f"{i} x {j} = {i*j}")

li = """Htwwjhy~ Z W xt Ljsnzx!! N lnaj Z uwjxjsy ktw ufxxnsl ymnx Vzjxy~ Gzy Dtz Mfaj Yt Xfd 'RTTDFMT' yt Rd Pfpft Yfqp Fhhtzsy. Mfmf~~"""
K = int(input("수 입력 : "))
for i in li.split() :
    for j in i:
        if 65<=ord(j)<=90 :
            if ord(j)-K<65 :
                j = chr(90-K+1)
            else :
                j = chr(ord(j)-K)
        elif 97<= ord(j)<=122:
            if ord(j)-K<97 :
                j = chr(90-K+1)
            else :
                j = chr(ord(j)-K)
        else :
            pass


        
        print(j, end=" ")



# A ~ Z > 65 ~ 90
# a ~ z > 97 ~ 122




























