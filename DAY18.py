# import requests
# from bs4 import BeautifulSoup

# res = requests.get("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTEwMjdfOTUg%2FMDAxNTcyMTc4OTM5MjI4.d6rniwbFZsznfxEFQQpP_-lKGeFwOBWbH_mQ5r1xatMg.-XEUIvdVV-q6igR-ujg_MfbVSM4DrLknZzdjGwQwm5Ug.JPEG.euniiily%2F%25B5%25A8%25B7%25E7%25B3%25AA11%25C8%25AD040.jpg&type=sc960_832")

# soup = BeautifulSoup(res.text, "html.parser")

# f = open("IU.png", "wb")
# f.write(res.content)

# from PIL import Image # 흑백

# img = Image.open("IU.png")
# for i in range(960):
#     for j in range(428):
#         rgb = img.getpixel((i,j))
#         a = sum(rgb)//3
#         img.putpixel((i,j),(a,a,a))
# # img.save("IUblack.png")
# img.show()

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("chromedriver.exe")
# driver.get("https://www.naver.com")

# 네이버검색창 = driver.find_element(By.CSS_SELECTOR, '#query')
# 네이버검색창.send_keys("악동뮤지션")
# 네이버검색창.clear()
# 네이버검색창.send_keys("블랙핑크")

# 네이버검색버튼 = driver.find_element(By.CSS_SELECTOR, "#search_btn")
# 네이버검색버튼.click()

# 소속사 = driver.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.cs_common_module.case_empasis._au_people_content_wrap._people_star.color_3 > div.cm_content_wrap > div.cm_content_area._cm_content_area_profile > div > div.detail_info_wrap > div > dl > div:nth-child(1) > dd > a")
# print(소속사.text)

# 태그 지정 후 할 수 있는 메서드/필드
# 1. send_keys(x)  x를 집어넣음 (로그인, 검색)
# 2. click()       클릭해줌
# 3. text          텍스트 부분 검출
# 4. Clear()            입력창을 지워줌

# input()

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("chromedriver.exe")
# driver.get("https://hansh.pythonanywhere.com/sel/nium1/")

# butt = driver.find_element(By.CSS_SELECTOR, "body > button")
# for i in range(1000):
#    if i != 999:
#      butt.click()

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("chromedriver.exe")
# driver.get("https://hansh.pythonanywhere.com/sel/jejudo/")

# butt1 = driver.find_element(By.CSS_SELECTOR, "#python1")
# butt2 = driver.find_element(By.CSS_SELECTOR, "#python2")

# for i in range(500):
    # if i != 499:
#         butt1.click()
#         butt2.click()

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("chromedriver.exe")
# driver.get("https://hansh.pythonanywhere.com/sel/cal/")

# ans = driver.find_element(By.CSS_SELECTOR, "#val")
# ques = driver.find_element(By.CSS_SELECTOR, "#ques")
# butt = driver.find_element(By.CSS_SELECTOR, "body > button")

# for i in range(100):
#     A = ques.text.split("+")
#     B = int(A[0])+int(A[1])
#     ans.send_keys(f"{B}")
#     butt.click()
#     if i != 99:
#         ans.clear()

# input() # 창유지


