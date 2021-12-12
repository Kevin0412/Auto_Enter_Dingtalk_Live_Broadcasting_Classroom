import pyautogui as pg
import cv2
import numpy as np
import pytesseract
from PIL import Image
import os
import glob
def enter():
    pg.moveTo(960,100)
    pg.click()
    pg.moveTo(1390,250)
    pg.click()
def auto_enter():
    pic=pg.screenshot(region=(355,100, 55,30))
    img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
    cv2.waitKey(100)
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    string = pytesseract.image_to_string(image,lang='chi_sim')
    if len(string)!=0:
        if string[0]=="[":
            enter()
while(True):
    auto_enter()
    
#自动进入钉钉直播间第二版，文字识别，由于钉钉直播时会跳出“[xxx正在直播]xx课”一行字，由于文字识别不够准确，我就取了第一个字符"["
