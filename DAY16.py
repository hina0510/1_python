# import requests
# from bs4 import BeautifulSoup

# res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4")
# soup = BeautifulSoup(res.text, "html.parser")

# for i in soup.select("strong.name")[:10]:
#     print(i.text)

# import requests
# from bs4 import BeautifulSoup

# for k in ran(1,5):
#     res = requests.get(f"https://news.ycombinator.com/news?p={k}")
#     soup = BeautifulSoup(res.text, "html.parser")

#     for i in soup.select(".titleline>a"):
#         print(i.text)

# from bs4 import BeautifulSoup

# st = """<html>
#     <body>
#         <div id="hello1" one="kgit">안녕1</div>
#         <div class="hello2" two="bank">안녕2</div>
#         <div>
#             <span three="happy">안녕3</span>
#         </div>
#         <a href="https://www.naver.com" four="newyear">NAVER</a>
#     </body>
# </html>"""

# soup = BeautifulSoup(st, "html.parser")

# print(soup.select_one("#hello1").get("one"))  # 속성값
# print(soup.select_one(".hello2").get("two"))
# print(soup.select_one("span").get("three"))
# print(soup.select_one("a").get("href"))

# import requests

# res = requests.get("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTA0MDNfNTIg%2FMDAxNTU0MjYzNzkxMDQ1.usVJuuP08tPVDhDxpkG2dQs3S6g4Fr6w-hyrSkRoI0Mg.lPxfPxeEVe4BhYPkG6jz7NmzhIHhyKP2LampmZZuO_Ug.GIF.hanee218%2Fgiphy.gif&type=l340_165")


# # res.text(HTML)
# # res.content(바이너리값)
# f = open("피카츄.gif", "wb")
# f.write(res.content)

# import requests
# from bs4 import BeautifulSoup
# import os

# def 폴더생성(st):
#     if not os.path.isdir(st)
#         os.mkdir(st)

# def 제거(st):
#     for i in "/\\\"?*<>|:":
#         st = st.replace(i, "")
#     return st

# 폴더생성(웹툰)
# res =  requests.get("https://comic.naver.com/webtoon/weekdayList?week=mon")

# soup = BeautifulSoup(res.text, "html.parser")

# for i in soup.select(".thumb > a > img"):
#     웹툰제목 = 제거(i.get("title"))
#     경로 = i.get("src")
#     r = requests.get(경로)
#     f = open(f"웹툰/{웹툰제목}.png", "wb")
#     f.write(r.content)

# import os

# os.mkdir (폴더명)  # 폴더 생성
# not Bull값 반대로
# if not os.path.isdir("케이지"): # 케이지가 존재하지 않으면
#     os.mkdir("케이지")

# def 폴더생성(st):
#     if not os.path.isdir(st):
#         os.mkdir(st)

# import requests
# from bs4 import BeautifulSoup
# import os

# def 폴더생성(st):
#     if not os.path.isdir(st):
#         os.mkdir(st)

# def 제거(st):
#     for i in "/\\\"?*<>|:":
#         st = st.replace(i, "")
#     return st  

# for i in "mon", "tue", "wed", "thu", "fri", "sat", "sun":
#     폴더생성(f"웹툰/{i}")
#     res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={i}")

#     soup = BeautifulSoup(res.text, "html.parser")

#     for j in soup.select(".thumb > a > img"):
#         웹툰제목 = 제거(j.get("title"))
#         경로 = j.get("src")
#         r = requests.get(경로)
#         f = open(f"웹툰/{i}/{웹툰제목}.png", "wb")
#         f.write(r.content)

# from bs4 import BeautifulSoup

# st = """<html>
#     <body>
#         <div class="champ">
#             <span id="name">케넨</span>
#             <span id="hp">1000</span>
#             <span id="mp">0</span>
#         </div>
#         <div class="champ">
#             <span id="name">티모</span>
#             <span id="hp">800</span>
#             <span id="mp">100</span>
#         </div>
#         <div class="champ">
#             <span id="name">베이가</span>
#             <span id="hp">600</span>
#             <span id="mp">400</span>
#         </div>

#     </body>
# </html>"""

# soup = BeautifulSoup(st, "html.parser")

# for i in soup.select(".champ"):
#     print(i.select_one("#name"))
#     print(i.select_one("#hp"))
#     print(i.select_one("#mp"))
#     champs[n]=[h, m]
# print(champs)

# import requests
# from bs4 import BeautifulSoup

# res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4#")

# soup = BeautifulSoup(res.text, "html.parser")

# for i in soup.select(".title_box")[:15]:
#     print(i.select_one(".name").text, end = " ")
#     print(i.select_one(".sub_text").text)

# import requests
# from bs4 import BeautifulSoup


# res = requests.get("https://music.bugs.co.kr/chart")

# soup = BeautifulSoup(res.text, "html.parser")

# song = soup.select("th > .title")
# artist = soup.select(".left > p.artist")
# for i in range(len(song)):
#     print(f"{song[i].text}",end = "\t")
#     print(f"{artist[i].text}")

# for i in soup.select("tbody> tr"):
#     print(i.select_one(".title>a").text, end = " ")
#     print(i.select_one(".artist>a").text)

# import requests
# from bs4 import BeautifulSoup
# import os

# def 제거(st):
#     for i in "/\\\"?*<>|:":
#         st = st.replace(i, "")
#     return st  

# res = requests.get("https://lol.inven.co.kr/dataninfo/champion/")
# soup = BeautifulSoup(res.text, "html.parser")

# for i in soup.select(".champImage > a"):
#     name = 제거(i.get("title"))
#     link =  "https:" + i.select_one("img").get("src")
#     r = requests.get(link)
#     f = open(f"LOL/{name}.png", "wb")
#     f.write(r.content)
    
import requests
from bs4 import BeautifulSoup
import os

res = requests.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
soup = BeautifulSoup(res.text, "html.parser")

for i in soup.select(".pokemonicon"):
    name = i.select_one("span").text
    link = "https:" + i.select_one("img").get("src").replace("pokemonicon","pokemonimage")
    r = requests.get(link)
    f = open(f"pocketmon/{name}.png", "wb")
    f.write(r.content)














