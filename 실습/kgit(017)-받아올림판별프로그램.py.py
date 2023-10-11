# 두 수를 입력받고(0-99), 두 수를 더할때 받아올림이 발생하는지 하지 않는지
# 판별하는 프로그램을 작성하세요.

A = int(input("첫번째 수 입력 : "))
B = int(input("두번째 수 입력 : "))

# '%' 연산자는 다양하게 활용되니!! 꼭 익히길 바랍니다
A_tail = A % 10  
# A 의 1의 자리는 다음과 같이 10 과의 나머지 연산을 통해 뽑아낼 수 있습니다.
B_tail = B % 10

if A_tail + B_tail >= 10:
    print("받아올림이 발생합니다!!")

if A_tail + B_tail < 10:
    print("받아올림이 발생하지 않습니다!!")

