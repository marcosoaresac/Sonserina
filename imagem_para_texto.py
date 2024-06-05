import pytesseract
import cv2

imagem = cv2.imread("texto.JPG") #receber a imagem 

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe" #o caminho do executavel que vai transformar em texto

result = pytesseract.image_to_string(imagem) #recebe a imagem e converte em texto

print(result)
