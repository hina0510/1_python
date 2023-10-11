# 파일 입출력!

# f = open("a/test.txt", "w")

# open(A, B) A는 경로를 포함한 파일명, B는 권한

# 절대경로는 드라이브로부터의 경로(C:\, D:\. ':'필요함.), 상대경로는 현재경로 기준으로 하는 경로(다음 페이지)
# 권한은 쓰기(w)(파일 이름 없으면 생성, 있으면 갱신), 읽기(r) - 있는 파일 읽어야 함(경로 주의), 쓰기(덧붙여)(a)

# f = open("testa/a.txt", "w")
# f = open("testa/testb/b.png", "w")
# f = open("testa/testb/testc/c.csv", "w")

# for i in range(100):
#     f = open("test.txt", "w")
#     f.write("hello")

# f = open("test.txt", "w")
# for i in range(100):
#     f.write("hello")

# 코드 실행 했을 떄 2단.txt ~ 9단.txt 파일 생성

# for i in range(2,10) :
#     f = open(f"구구단/{i}단.txt", "w")
#     for j in range(1,10):
#         f.write(f"{i} x {j} = {i*j}\n")

# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕")

# 인코딩 (cp949(ANSI)) data > 0101010
# 디코딩 (UTF-8) 0101010 > data

# f = open("test.txt", "w", encoding="utf-8")
# for i in range(1,101) :
#     f.write(f"파이썬 존잼 {i}\n")

# f = open("test.txt", "r", encoding="utf-8")

# print(f.read()) # 파일 전체
# print(f.readline()) # 한줄 읽기 (다음 줄로 넘어감)
# print(f.readlines()) # 한줄한줄 리스트로

# for i in range(2,10):
#     f = open(f"구구단/{i}단.txt", "r", encoding="utf-8")
#     for j in range(1,10):
#         print(f.read()) # read는 단끼리 묶어서 출력, readline은 구구단 한줄씩 출력











