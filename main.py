import pyautogui as pg
import cv2
import numpy as np
imge=cv2.imread('enter.bmp')#读取之前截取的图片
while(True):
    pic=pg.screenshot(region=(80,50, 20,20))#截取弹出正在直播的图标的位置
    img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
    cv2.waitKey(100)
    k=0
    for x in range(20):
        for y in range(20):
            for z in range(3):
                if abs(int(img[x,y,z])-int(imge[x,y,z]))>0:
                    k+=1#与之前的截图对比
    #print(k)
    if k==0:#如果和之前截图相同
        pg.moveTo(90,60)#鼠标移动至进入直播间的按钮的位置
        pg.click()#鼠标点击
        pg.moveTo(1450,250)#鼠标移动至直播间窗口最大化的位置
        pg.click()#鼠标点击
        pg.moveTo(800,500)#鼠标移动到直播间窗口内
        pg.click()#鼠标单击开始观看直播
