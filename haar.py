import cv2
import numpy as np

#HAARCASCADE
plate_cascade = cv2.CascadeClassifier('placas-modelo-antigo.xml')

#RECEBE A IMAGEM
entrada = cv2.imread(r"BD3\1.jpg")

#REDIMENSIONA A IMAGEM
#entrada = cv2.resize(entrada, (800, 600))

#TRANSFORMA EM ESCALAS DE CINZA
gray = cv2.cvtColor(entrada, cv2.COLOR_BGR2GRAY)
cv2.imshow('cinza',gray)
cv2.waitKey()

#APLICA O HAARCASCADE
#faces = plate_cascade.detectMultiScale(gray, 6.5,17)
plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=10, minSize=(60,60),flags=cv2.CASCADE_SCALE_IMAGE)

#PERCORRE O VETOR HAAR
for (x,y,w,h) in plates:
    #PLACA RECEBE O RECORTE COM ALTURA E LARGURA
    placa = entrada[y:y + h, x:x + w]
    #DESENHA O RETANGULO DA PLACA
    cv2.rectangle(entrada, (x, y), (x + w, y + h), (0, 255, 0), 2)

#MOSTRA A IMAGEM
cv2.imshow('img',entrada)
cv2.imwrite("PLACAdesenhada.jpg",entrada)
cv2.waitKey()

#MOSTRA E SALVA A IMAGEM DA PLACA
cv2.imshow('img',placa)
cv2.imwrite("PLACA.jpg",placa)
cv2.waitKey()


cv2.destroyAllWindows()