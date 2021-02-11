import pytesseract as ocr
import cv2
import tkinter
from PIL import Image
from PIL import ImageOps
import numpy as np

#RECEBE A IMAGEM
img = cv2.imread("placa.jpg")
cv2.imshow("ENTRADA", img)
cv2.waitKey(0)

#RECEBE AS MEDIDAS DA IMAGEM
#print ("Altura (height): " ,(img.shape[0]))
#print ("Largura (width): " , (img.shape[1]))
#print ("Canais (channels): ", (img.shape[2]))
alt = (img.shape[0])
lar = (img.shape[1])
metade = (img.shape[1] / 2)
#print(metade)
if metade < 110:
    novametade = ((img.shape[1] / 2) -10)
else:
    novametade = ((img.shape[1] / 2) -15)
print(novametade)

#DIVIDE A IMAGEM AO MEIO
char = img[0:int(alt), 0: int(novametade+10)]
cv2.imshow("metade1", char)
#cv2.imwrite("PLACAletras.jpg",char)
cv2.waitKey(0)
num = img[0:int(alt), int(novametade-10):int(lar)]
cv2.imshow("metade2", num)
#cv2.imwrite("PLACAnumeros.jpg",num)
cv2.waitKey(0)

# REDIMENSIONA A IMAGEM
img = cv2.resize(img,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
char = cv2.resize(char,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
num = cv2.resize(num,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)

#APLICA MELHORIAS NA IMAGEM
#CONVERTE EM TONS DE CINZA
#num = cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)
#APLICA O BLUR
#num = cv2.GaussianBlur(num,(3,3),10)
#BINARIZA
#num = cv2.threshold(num, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#th,thresh1 = cv2.threshold(num,70, 255,cv2.THRESH_BINARY)
#CRIA UM KERNEL
kernel = np.ones((7,7), np.uint8)
#APLICA EROSÃO
num = cv2.erode(num, kernel, iterations=2)
#APLICA A DILATAÇÃO
num = cv2.dilate(num, kernel, iterations=2)
#cv2.imwrite("PLACAnum.jpg",num)

#APLICA MELHORIAS NA IMAGEM
#CONVERTE EM TONS DE CINZA
char = cv2.cvtColor(char, cv2.COLOR_BGR2GRAY)
#APLICA O BLUR
char = cv2.GaussianBlur(char,(3,3),10)
#BINARIZA
char = cv2.threshold(char, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#th,thresh1 = cv2.threshold(num,70, 255,cv2.THRESH_BINARY)
#CRIA UM KERNEL
kernel = np.ones((7,7), np.uint8)
#APLICA EROSÃO
char = cv2.erode(char, kernel, iterations=2)
#APLICA A DILATAÇÃO
char = cv2.dilate(char, kernel, iterations=2)
#cv2.imwrite("PLACAchar.jpg",char)


#TESSERACT APLICA A LEITURA
ocr.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
letras = ocr.image_to_string(char, lang='eng2', config='--psm 12 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ocr.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
numeros = ocr.image_to_string(num, lang='digits_comma', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
#ocr.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#placa = ocr.image_to_string(img, lang='por', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

#PROCURA POR CARACTERES ESPECIAIS E RETIRA DA STRING
str = "!@#%¨&*()_+:;><^^}{`?|[]~¬\/=,.'ºª»‘áàéèiíìóòúù♀️"
for x in str:
    letras = letras.replace(x, '')
    numeros = numeros.replace(x,'')
print(numeros)
print(letras)

#PEGA SÓ A QUANTIDADE DE 3 LETRAS E 4 NUMEROS
letras = letras[0:3]
numeros = numeros[0:4]
placa = letras + numeros
print(placa)

#ABRE A JANELA COM O RESULTADO
janela = tkinter.Tk()
tkinter.Label(janela, text=placa, font=("Helvetica", 25)).pack()
janela.mainloop()