def detectBorder(img, maxWidth = 35):
    #IDENTIFICAR OS GLÓBULOS BRANCOS
    import cv2
    import numpy as np

    hsv_img = cv2.cvtColor(img, cv2.COLOR_LBGR2LAB)
    valor_minimo1 = np.array([130, 146, 20])
    valor_maximo1 = np.array([255, 255, 180])
    mask = cv2.inRange(hsv_img, valor_minimo1, valor_maximo1)
    contourns, lx = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ROIs = []
    if len(contourns) != 0:
        for contour in contourns:
            x, y, w, h = cv2.boundingRect(contour)
            if w > maxWidth:
                ROIs.append(img[y: y+h, x: x+w])
    grayROIs = []
    for corte in ROIs:
        grayROIs.append(cv2.cvtColor(corte, cv2.COLOR_BGR2GRAY))
    return grayROIs

def showImage(*figs):
    #MOSTRAR VÁRIAS IMAGENS
    from cv2 import imshow, waitKey
    txts = []
    imgs = []
    for cont in range(0, len(figs)):
        if cont % 2 == 0:
            txts.append(figs[cont])
        if cont % 2 == 1:
            imgs.append(figs[cont])
        
    for a in range(0, len(txts)):
        imshow(txts[a], imgs[a])
    
    waitKey(0)

def resizeImg(img, size):
    #MODIFICAR TAMANHO DA IMAGEM
    from cv2 import resize, INTER_AREA
    width = img.shape[1]
    height = img.shape[0]
    proportion = (width / height)
    new_width = size
    new_height = int(new_width * proportion)
    new_size = (new_height, new_width)
    new_img = resize(img, new_size, interpolation= INTER_AREA)

    return new_img


def status(img, showCanal = False, y = -1, x = -1):
    #STATUS DA IMAGEM
    print('Altura:', img.shape[0])
    print('Largura:', img.shape[1])
    if showCanal:
        print('Quantidade de canais:', img.shape[2])
        
    if y > -1 and x > -1:
        (r, g, b) = img[y, x]
        print('vermelho:', r)
        print('verde:', g)
        print('azul:', b)