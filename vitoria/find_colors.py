import cv2
import numpy as np
roi = cv2.imread('')
hsvRoi = cv2.cvtColor(roi, cv2.COLOR_LBGR2LAB)
print('min H = {}, min S = {}, min V = {}; max H = {}, max S = {}, max V = {}'.format(hsvRoi[:, :, 0].min(),
hsvRoi[:, :, 1].min(),
hsvRoi[:, :, 2].min(),
hsvRoi[:, :, 0].max(),
hsvRoi[:, :, 1].max(),
hsvRoi[:, :, 2].max()))

cv2.waitKey(0)
