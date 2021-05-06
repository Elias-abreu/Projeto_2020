import cv2
import numpy as np

lower = np.array([130, 146, 20])
upper = np.array([255, 255, 180])

img = cv2.imread('Resources/WIN_20201026_10_15_10_Pro.jpg')
blur = cv2.GaussianBlur(img, (7, 7), 0)
img2 = cv2.cvtColor(blur, cv2.COLOR_LBGR2LAB)
mask = cv2.inRange(img2, lower, upper)
objeto, lx = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(objeto) != 0:
        for objeto in objeto:
            x, y, w, h = cv2.boundingRect(objeto)
            if w > 200:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

mask = cv2.resize(mask, (600,600))
cv2.imshow("mask", mask)

img = cv2.resize(img, (600,600))
cv2.imshow("imagem", img)

cv2.waitKey(0)