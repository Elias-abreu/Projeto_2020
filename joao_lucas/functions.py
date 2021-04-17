def showImage(*figs):
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
    from cv2 import resize, INTER_AREA
    width = img.shape[1]
    height = img.shape[0]
    proportion = (width / height)
    new_width = size
    new_height = int(new_width * proportion)
    new_size = (new_height, new_width)
    new_img = resize(img, new_size, interpolation= INTER_AREA)

    return new_img


def status(img, cn = False, y = -1, x = -1):
    print('Altura:', img.shape[0])
    print('Largura:', img.shape[1])
    if cn:
        print('Quantidade de canais:', img.shape[2])
        
    if y > -1 and x > -1:
        (r, g, b) = img[y, x]
        print('vermelho:', r)
        print('verde:', g)
        print('azul:', b)