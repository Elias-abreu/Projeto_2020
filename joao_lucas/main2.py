import numpy as np
import cv2

diretorio = '../Imagens_a_serem_analisadas/'
nome_img1 = 'eusinofilo_01'
nome_img2 = 'eusinofilo_04'
nome_img3 = 'monocitos_01'
nome_img4 = 'neutrofilo_01'
nome_img5 = 'WIN_20201026_10_15_10_PRO'

imgColorida = cv2.imread(diretorio + nome_img5 + '.jpg') #Carregamento da imagem
#Se necessário o redimensioamento da imagem pode vir aqui.

#Passo 1: Conversão para tons de cinza
img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)
largura = int(img.shape[0] / 4)
altura = int(img.shape[1] / 4)

#Passo 2: Blur/Suavização da imagem

suave = cv2.GaussianBlur(img, (7, 7), 0)

#outra forma de binarizar a imagem
ret2, binn2 = cv2.threshold (suave.copy(), 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)




#Removendo ruído
kernel = np.ones((3, 3), np.uint8)
binn2 = cv2.morphologyEx(binn2, cv2.MORPH_OPEN, kernel, iterations = 2)



kernel = np.ones((5,5),np.uint8)
erosao = cv2.erode(binn2,kernel,iterations = 1)

kernelD = np.ones((9,9),np.uint8)
dilation = cv2.dilate(erosao,kernelD,iterations = 1)


bordas = cv2.Canny(dilation, 20,120,apertureSize = 7)

(objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


imgC2 = imgColorida.copy()
celulas_vermelhas = []

contadorVermelha = 0

for i in objetos:
    x, y, w, h = cv2.boundingRect(i)
    ROI = imgC2[y:y+(h), x:x+(w)]#pegar uma imagem do cortorno

    larguraR = int(ROI.shape[0] / 4)
    alturaR = int(ROI.shape[1] / 4)

    
    if(20 < larguraR < 100) or (20 < alturaR < 100):
        celulas_vermelhas.append(i)
        contadorVermelha += 1


cv2.drawContours(imgC2, celulas_vermelhas, -1, (255, 0, 0), 7)



#Redimencionar as imagens
imgColorida2 = cv2.resize(imgColorida, (altura, largura))
imgC2 = cv2.resize(imgC2, (altura, largura))

cv2.imshow(f'Vermelhas {contadorVermelha}, {nome_img5}', imgC2)
cv2.waitKey(0)

cv2.imwrite(nome_img5 + '(copia).jpg', imgC2)

