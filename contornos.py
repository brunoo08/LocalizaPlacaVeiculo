import numpy as np
import cv2
from matplotlib import pyplot as plt
from time import sleep 

def showImage(img):
    # REDIMENSIONA IMAGEM
    #img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    # DIMINUI A IMAGEM
    #img = img[::2, ::2]
    cv2.imshow("Resultado", img)
    # SALVA A IMAGEM COM OS FILTROS APLICADOS
    #cv2.imwrite("Results/AreaEncontrada.jpg",img)
    cv2.waitKey(0)
    
def main():
    original = cv2.imread(r"BD3/111.jpg")
    showImage(original)
    #TONS DE CINZA
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    #showImage(gray)
    #BINARIZAÇÃO
    ret, img = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
    #showImage(img)
    #GAUSSIAN BLUR
    img = cv2.GaussianBlur(img,(5,5),0)
    showImage(img)
    cv2.imwrite("imgcomFiltros.jpg", img)
    #PROCURA CONTORNOS
    contornos,hier = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #cv2.drawContours(original, contornos, -1, (0,255,0), 3)
    #cv2.imwrite("exemploDraw.jpg",original)
    showImage(original)
    # PROCURA CONTORNOS QUADRADOS
    roi = original
    for c in contornos:
        # VERIFICA SE É UM CONTORNO FECHADO
        fechado = cv2.arcLength(c, True)
        if fechado > 300:
            # APROXIMA A FORMA PRA UM "QUADRADO"
            aprox = cv2.approxPolyDP(c, 0.03* fechado, True)
            # VERIFICA SE TEM 4 CANTOS
            if len(aprox) == 4:
                #  SE IMAGEM RETA OU CONTORNOS RETOS
                (x, y, alt, lar) = cv2.boundingRect(c)
                cv2.rectangle(original, (x, y), (x + alt, y + lar), (0, 255, 0), 3)
                cv2.imwrite("exemploDrawespecifico.jpg",original)
                roi = img[(y+15):y+lar, x:x+alt]
                '''# SE IMAGEM TORTA OU CONTORNOS NÃO RETOS
                rect = cv2.minAreaRect(c)
                caixa = cv2.boxPoints(rect)
                box = np.int0(caixa)
                original = cv2.drawContours(original, [box], -1, (0, 0, 255), 3)'''

    showImage(original)

# EXECUTA O CÓDIGO
main()