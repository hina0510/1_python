# A-B-C-D 순서로 돌아가면서 한 명당  청소를 하기로 했다, 첫 날은 A 가 청소를 한다고 했을 때, N 일째 당번은 누구인가?
# 아무리~~~ 큰 수도 4가지 상황에서 돌게되어있어요
# %4 를 하면 0, 1, 2, 3 네가지가 나옵니다!!
# 각각에 맞게 매칭만 시켜주시면되요!

N = int(input("몇 일?"))

if N % 4 == 1:
    print("A")
elif N % 4 == 2:
    print("B")
elif N % 4 == 3:
    print("C")
else:
    print("D")
