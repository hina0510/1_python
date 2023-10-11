# 크롤링
#<1>
# import requests

# res = requests.get("http://www.naver.com")
# URL로 request 를 보냄. response를 반환
# res.text > HTML 문서

# HTML : 태그(여는 태그<>와 닫는 태그</>), 속성, 속성값, 텍스트
# 파싱 : 웹의 규격에 맞춰서 해석함

#<2>
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(문자열, "html.parser")
# from bs4 import BeautifulSoup

# st = """<html>
#     <body>
#         <div id="hello1">안녕1</div>
#         <div class="hello2">안녕2</div>
#         <div>
#             <span>안녕3</span>
#         </div>
#         <a href="https://www.naver.com">NAVER</a>
#     </body>
# </html>"""

# soup = BeautifulSoup(st, "html.parser")
# st 를 웹의 언어로 소통할 수 있는 soup 생성


#<3>
# 셀렉터(태그를 지칭하는 방법)
# 태그 그대로, id# , class. , 하위태그 >

# print( soup.select("a"))
# print( soup.select("#hello1"))
# print( soup.select(".hello2"))
# print(soup.select("div > span"))

# import requests
# from bs4 import BeautifulSoup

# for i in range(1,112) :
#     res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=758037&no={i}&weekday=mon")

#     soup = BeautifulSoup(res.text, "html.parser")

#     print(soup.select_one("#topPointTotalNumber>strong").text)
#     print(soup.select_one(".pointTotalPerson>em").text)
#     print(soup.select_one(".date").text)

# 더블클릭 후 복사
# ctrl + f

#<4>
# soup.select > 태그들(태그 클래스의 인스턴스 리스트) soup.select_one > 태그(첫번째)(태그 클래스의 인스턴스)
# .text > soup.select_one 에서 사용가능

# from bs4 import BeautifulSoup

# st = """<html id="b">
#     <body class="c">
#         <div id="hello1">안녕1</div>
#         <div class="hello2">안녕2</div>
#         <div>
#             <span id="hello1">안녕3</span>
#         </div>
#         <a href="https://www.naver.com">NAVER</a>
#     </body>
# </html>"""

# soup = BeautifulSoup(st, "html.parser")
# print(soup.select_one("#hello1").text)
# print(soup.select_one(".hello2").text)
# print(soup.select_one("span#hello1").text)
# print(soup.select_one("a").text)

# import requests
# from bs4 import BeautifulSoup
# for i in range(1,163):
#     res = requests.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={i}")

#     soup = BeautifulSoup(res.text, "html.parser")


# print(soup.select_one(".korName").text.split(",")[0], end="\t")
# print(soup.select_one(".rp").text, end="\t")
# print(soup.select_one(".ip").text, end="\t")







