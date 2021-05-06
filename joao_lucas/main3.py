import cv2
import numpy as np 
from functions import *


img = cv2.imread('../Imagens_a_serem_analisadas/eusinofilo_04.jpg')


hsv_img = cv2.cvtColor(img, cv2.COLOR_LBGR2LAB)
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


valor_minimo1 = np.array([130, 146, 20])
valor_maximo1 = np.array([255, 255, 180])

valor_minimo2 = np.array([165,140,96])
valor_maximo2 = np.array([219,166,124])

mask = cv2.inRange(hsv_img, valor_minimo1, valor_maximo1)

contourns, lx = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contourns) != 0:
    for contour in contourns:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 200:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)


img = resizeImg(img, 600)

cv2.imshow('Result', img)
cv2.waitKey(0)