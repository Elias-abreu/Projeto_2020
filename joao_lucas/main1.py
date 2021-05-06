import cv2
from functions import *

diretorio = './Imagens_a_serem_analisadas/'
nome_img = 'eritrocitos_01'

img = cv2.imread(diretorio + nome_img + '.jpg')

img = resizeImg(img, 600)

grayScaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurImg = cv2.bilateralFilter(grayScaleImg, 9, 75, 75)
cannyImg = cv2.Canny(blurImg, 10, 60)


contours, lx = cv2.findContours(cannyImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


celulas_vermelhas = []
for i in contours:
    x, y, w, h = cv2.boundingRect(i)
    ROI = img[y:y+(h), x:x+(w)]#pegar uma imagem do cortorno

    larguraR = int(ROI.shape[0] / 4)
    alturaR = int(ROI.shape[1] / 4)

    
    if (larguraR > 10 and larguraR < 100) or (alturaR > 10 and alturaR < 100):
        celulas_vermelhas.append(i)

cv2.drawContours(img, celulas_vermelhas, -1, (0,0,255), 2)

showImage('Eritrocito', img)

# cv2.imwrite(nome_img + '(copia).jpg', img)
