#仅限钉钉电脑版，全屏模式，具体进入退出按钮位置因电脑而异。
import pyautogui as pg
import time
import datetime
def enter():
    pg.moveTo(960,150)#进入直播按钮坐标，可自行调整
    pg.click()
def exit():
    pg.moveTo(960,840)#退出直播按钮坐标，可自行调整
    pg.click()
now_time=datetime.datetime.now().strftime('%R')
def Auto_enter(Time):#10秒一次尝试点击
    time.sleep(10)
    if now_time==Time:
        enter()
        print("enter,"+str(now_time))
def Auto_exit(Time):
    if now_time==Time:
        exit()
        print("exit,"+str(now_time))
    time.sleep(10)
while(True):
    for m in range(5):
        Auto_enter("07:"+str(35+m))
        Auto_exit("12:35")
        Auto_enter("12:"+str(35+m))
        for a in range(3):
            if a==2:
                Auto_exit(str(8+a)+":"+str(25))
                Auto_enter(str(8+a)+":"+str(25+m))
            else:
                Auto_exit("0"+str(8+a)+":"+str(25))
                Auto_enter("0"+str(8+a)+":"+str(25+m))
            Auto_exit(str(13+a)+":"+str(25))
            Auto_enter(str(13+a)+":"+str(25+m))
            if a==0:
                Auto_exit("0"+str(9+a)+":"+str(10+m))
                Auto_enter("0"+str(9+a)+":"+str(10+m))
            else:
                Auto_exit(str(9+a)+":"+str(10+m))
                if a==1:
                    Auto_enter(str(9+a)+":"+str(10+m))
            Auto_exit(str(14+a)+":"+str(10+m))
            if a!=2:
                Auto_enter(str(14+a)+":"+str(10+m))
    now_time=datetime.datetime.now().strftime('%R')
    print(now_time)
