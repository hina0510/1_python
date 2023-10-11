# 년도를 입력받고, 윤년인지 아닌지 판별하는 프로그램
# (4의 배수이지만, 100의 배수는 윤년이 아닙니다. 하지만, 400의 배수는 윤년이라고 합니다.)
# 수업시간에서 각각의 조건에 대해서 분석해봤죠?

년도 = int(input("연도를 입력하세요 :"))

# 4의 배수는 윤년이라고 말할 수 있나요?
# 아니죠!! 100의 배수는 윤년이 아니기 때문이에요
# 100의 배수는 윤년이 아니라고 할 수 있나요?
# 아니에요!! 400의 배수는 윤년이기 때문이죠!!
# 그렇다면 400의 배수는 윤년인가요?
# 맞죠! 제일 확실한 조건입니다. 맨위에 적어주죠~
if 년도 % 400 == 0:
    print("윤년입니다.")
# 자!! 400 의 배수는 여기서 걸러집니다.
# 즉, 400의 배수가 아닌 친구들이 내려온다는 거죠!!
# 400의 배수 조건은 없다고 가정할때!

# 4의 배수는 윤년이라고 말할 수 있나요?
# 아니죠!! 아직도 100 의배수 조건이 있어요ㅜㅜ
# 그렇다면 이제는 100의 배수이면 평년이라고 말할 수 있나요?
# 맞죠!!!
elif 년도 % 100 == 0:
    print("평년입니다.")
# 이제야 비로소 4의 배수는 윤년이라고 말할 수 있는거에요!
elif 년도 % 4 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")


