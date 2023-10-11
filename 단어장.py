import os

dic = {}
# f = open("word.txt", "r", encoding="utf-8")
# for i in f.read().split():
#     E = i.split(":")
#     dic[E[0]] = E[1]

# 나만의 단어장 만들기 프로그램
D = 0
while True:
    print("="*30)  # ===============
    print("1. 단어검색")  # 1. 단어검색
    print("2. 단어추가")  # 2. 단어추가
    print("3. 단어수정")  # 3. 단어수정
    print("4. 단어삭제")  # 4. 단어삭제
    print("5. 종료")  # 5. 종료
    print("="*30)  # ===============
    A = int(input("메뉴입력 > "))  # 메뉴입력 > 1
    if A == 1:
        B = input("검색할 단어를 입력해주세요 : ")  # 검색할 단어를 입력해주세요 : apple
        if B in dic :
            print(B, "의 뜻은", dic[B], "입니다.")
        else :
            print("등록된 단어가 아닙니다.")

    elif A == 2 : 
        B = input("검색할 단어를 입력해주세요 : ")  # 검색할 단어를 입력해주세요 :
        if B in dic :
            D += 1
            if D > 1 :
                print("이미", dic[B], "라고 저장이 되어있어요!!")
            else :
                print("이미 등록된 단어입니다.")
        else :
            print(B, "의 뜻을 입력해주세요:", end= "")
            C = input("")  # air 의 뜻을 입력해주세요 : 
            dic[B] = C
            print("단어 추가 완료!!")

    elif A == 3 :
        B = input("수정할 단어를 입력해주세요 : ")  # 수정할 단어를 입력해주세요 : air
        if B in dic :
            print(B, "의 뜻을 입력해주세요:", end= "")   # air 의 뜻을 입력해주세요 : 
            C = input("")
            dic[B] = C
            print("단어의 뜻이 수정되었습니다!!")  # 단어의 뜻이 수정되었습니다!!
        else :
            print("등록되지 않은 단어입니다.") # 등록되지 않은 단어입니다.

    elif A == 4 :
        B = input("검색할 단어를 입력해주세요 : ")
        if B in dic :
            del dic[B]
            print(B, "가 사전에서 삭제됩니다.")
        else :
            print("등록되지 않은 단어입니다.")
            
    elif A == 5 :
        print("빠잇!")
        break
    else :
        print("메뉴를 입력하세요.")

os.system("cls")
f = open("word.txt", "w", encoding="utf-8")
f.write(f"{B} : {C}\n") # 종료 시 단어장에 저장됨
    



