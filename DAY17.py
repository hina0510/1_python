# import os

# for i in "mon", "tue", "wed", "thu", "fri", "sat", "sun":
#     print(i, len(os.listdir(f"웹툰/{i}")))

# os.listdir(x) x 아래의 파일/폴더 이름을 리스트로 반환

# for i in os.listdir("구구단"):
#     f = open(f"구구단/{i}", "r")
    
# os.rename(A, B) A 는 바꾸고자 하는 파일, B 는 바꿀 이름
# for i in os.listdir("실습"):
#     번호 = i.split("_")[0]
#     이름 = i[4:]
#     바꿀이름 = f"kgit({번호})-{이름}.py"
#     os.rename(f"실습/{i}", f"실습/{바꿀이름}")

#문자열.zfill(수)

# for i in os.listdir("pocketmon"):
#     A = i.split(".")
#     ch = f"{A[0].zfill(3)}_{A[1][:-1]}.png"
#     os.rename(f"pocketmon/{i}", f"pocketmon/{ch}")

# from PIL import Image

# img =  Image.open(f"pocketmon/001_이상해씨.png")
# img = img.resize((500,500))
# img.show() #현재 이미지 상태 확인
# img.save("a/거다이맥스이상해씨.png")

# from PIL import Image
# import os

# for i in os.listdir("pocketmon"):
#     img = Image.open(f"pocketmon/{i}")
#     img = img.resize((500,500))
#     img.save(f"poke500/{i}")

# from PIL import Image

# img = Image.open(f"poke500/491_다크라이.png")

# print(img.mode) # 색상모드 RGB, RGBA 0(투명)-255(선명)

# print(img.getpixel((0,0)))   # 0,0 의 색상정보를 반환
# print(img.getpixel((250,250)))   # 250,250 의 색상정보를 반환

# for i in range(500):
#     for j in range(500):
#         rgba = img.getpixel((i,j))
#         if rgba[3]>100:
#             # print(rgba)
#             img.putpixel((i,j), (0,0,0,255))
# 0,0 에 색상을 255,0,0,255 빨간색으로 넣어줌
# img.show()

from PIL import Image
import os

for i in os.listdir(f"poke500"):
    img = Image.open(f"poke500/{i}")
    for j in range(500):
        for k in range(500):
            rgba = img.getpixel((j,k))
            if rgba[3]>100:
                img.putpixel((j,k), (0,0,0,255))
    img.save(f"pokedark/{i}")


