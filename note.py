import pyautogui as pg
import cv2
import numpy as np
pic=pg.screenshot(region=(80,50, 20,20))#截取弹出正在直播的图标的位置
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
cv2.waitKey(100)
cv2.imwrite('enter.bmp',img)#保存图片
