# 시간과 분을 입력받고, 30분 전 시간을 출력해주는 프로그램

hour = int(input("시간 입력 : "))
min_ = int(input("분 입력 : "))

# 자 우선은 시간을 모두 분으로 환산 하고 나중에 시간, 분으로 나눠주는 방법으로 
# 푸는게 제일 깔끔해요! 왜냐하면 min_ < 30 이런 조건들을 해줘야 하기 때문이죠!
총분 = hour*60 + min_ - 30
# 여기서 문제는 0 시 20 분의 경우에는 23 시 50 분이 나와야한다는 것입니다.
# 즉! 30 분을 뺏을 때 음수일경우를 처리해주어야합니다.
if 총분 < 0:
    총분 += 1440
print("30 분전 시간 :",총분//60,"시간",총분%60,"분")
# 하루에 최대한 가질수 있는 분을 더해버리면 되겠죠?
    # 0 보다 클경우는 고민안해도되요

