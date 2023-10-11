import turtle as t
import random as r
import time
import dy

dic = dy.d

t.ht() # 커서 숨김
t.setup(1400,800) # 해상도 왼쪽 아래쪽에 쏠리게
t.colormode(255)
t.speed(0)
t.pu()

for i in dic:
    if dic[i] > 1:
        num += 1
    t.goto(r.randint(-650,500),r.randint(-300,200))
    t.color((r.randint(0,255), r.randint(0,255), r.randint(0,255)))
    t.write(i, font = ("맑은고딕", (dic[i]+10)*2, "bold"))
    if num % 5 == 0 :
        time.sleep(1)


















t.mainloop() # 창을 유지, 항상 맨 밑에