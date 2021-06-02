import cv2
from os import listdir
import joao_lucas.modules as fc

diretorioBaso = '../Main_Dataset/Baso'
diretorioEosi = '../Main_Dataset/eosi'
diretorioLymp = '../Main_Dataset/lymp'
diretorioMixt = '../Main_Dataset/mixt'
diretorioMono = '../Main_Dataset/mono'
diretorioNeut = '../Main_Dataset/neut'


diretorioFinal = './resultados_3/mixt'
fileType = '.bmp'
files = []

diretorio = listdir(diretorioMixt)
for file in diretorio:
    if file.endswith(fileType):
        files.append(file)

resultado = []
for file in files:
    img = cv2.imread(diretorioMixt+'/'+file)
    resultado.append(fc.detectBorder(img, 25))

cont = 0
for index, elemento in enumerate(resultado):
    for el in elemento:
        fc.showImage(f'img_{index}', el)
        cv2.destroyAllWindows()
        cv2.imwrite(f'{diretorioFinal}/img_{cont}.png', el)
        cont += 1

