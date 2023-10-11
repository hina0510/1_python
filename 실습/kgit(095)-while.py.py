# 반복문에는 for 와 while 이 있습니다.
# 물론 문제에 따라 같은 기능을 하게 만들어 줄 순 있습니다.
# 하지만, for 와 while 은 그 성질이 아주 확연하게 다릅니다.

# for 는 반복 횟수가 확실할 경우 사용합니다.
# 순서있는 자료형 만큼의 반복 횟수를 가지기 때문입니다.

# 이에 반해, while 은 반복횟수가 명확하지 않은 경우 
# 자주 사용하게 됩니다.

# 기본형식은 다음과 같습니다.
'''
while [ Bool ]:
    [      while 의 종속문장         ]

'''
# Bool 값이 참일 때 동안 종속문장을 반복합니다.
# 자!! Bool 값하면 생각나는 것들이 있죠?
# 13, 14 번 file 에서 다시 복습하고 오도록하세요!

# 자, 다음코드를 볼까요?
'''
while True:
    if [ 사용자가 종료를 원한다. ]:
        break
'''
# 실제로 while 은 다음과 같은 형태로 주로 쓰입니다.
# while True: 
# Bool 값이 True 이므로 계속 반복실행됩니다. 이를 무한반복문이라고 불러요.
# break 라는 녀석은 반복문을 탈출할 수 있도록 해주는 구문입니다.
# 사용자가 종료를 원한다가 True 이면 무한반복문을 나가도록 해주죠.

'''

while True:
    if [   사용자가 로그인을 한다.    ]:
        break
'''
'''
while True:
    if [    화면을 터치한다.    ]:
        break
'''
# 위와 같은 형태로 쓰이지요!! 왜냐하면 사용자가 언제 입력할지
# 모르기 때문에 혹은 언제 화면을 터치할지 모르기 때문에
# 정확한 반복횟수를 모르니까요!!!!!

# 자, 근데 while 에서는 특히 프로그램의 실행 순서를
# 잘 파악하셔야해요!!!!
# 꼭입니다 꼭!!!
