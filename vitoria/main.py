import numpy as np
import cv2
import mahotas

def escreve(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0,
    cv2.LINE_AA)
imgColorida = cv2.imread('Resources/WIN_20201026_10_15_10_Pro.jpg')

img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(img, (7, 7), 0)

ret2, bin = cv2.threshold (suave.copy(), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

bordas = cv2.Canny(bin, 70, 150)

objetos, lx = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
listaCelulas = []
for i in objetos:
    x, y, w, h = cv2.boundingRect(i)
    ROI = imgColorida[y:y + (h), x:x + (w)]  # pegar uma imagem do cortorno
    larguraR = int(ROI.shape[0] / 4)
    alturaR = int(ROI.shape[1] / 4)
    if(larguraR > 20):
        listaCelulas.append(i)

cv2.waitKey(0)
cv2.drawContours(imgColorida, listaCelulas, -1, (255, 0, 0), 10)
#escreve(img, str(len(listaCelulas))+" objetos encontrados!")
imgColorida = cv2.resize(imgColorida, (600,600))
cv2.imshow("Resultado "+str(len(listaCelulas)), imgColorida)
#cv2.imshow("Resultado ", imgColorida)
cv2.waitKey(0)