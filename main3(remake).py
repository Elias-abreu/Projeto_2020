import cv2
import numpy as np 
import joao_lucas.modules as fc


img = cv2.imread('../Imagens_a_serem_analisadas/Linfocito_Neutrofilo.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_LBGR2LAB)

valor_minimo1 = np.array([130, 146, 20])
valor_maximo1 = np.array([255, 255, 180])

mask = cv2.inRange(hsv_img, valor_minimo1, valor_maximo1)

contourns, lx = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

ROIs = []

if len(contourns) != 0:
    for contour in contourns:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 200:
            ROIs.append(img[y: y+h, x: x+w])

grayROIs = []
for corte in ROIs:
    grayROIs.append(cv2.cvtColor(corte, cv2.COLOR_BGR2GRAY))


fc.showImage(
    'Img 1', grayROIs[0], 
    'Img 2', grayROIs[1]
)
#cv2.imwrite(nome_img5 + '(copia).jpg', imgC2)