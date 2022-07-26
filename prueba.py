rom PIL import PdfImagePlugin , Image
from pytesseract import * 
import cv2
from pdf2image import *
import os
#IA
pytesseract.tesseract_cmd = r'C:\Users\Usuario\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#pasar de pdf a img
pdf = "ADMIN1 APR.pdf"
pdf_imagen=convert_from_path(pdf,500,poppler_path=r'C:\Program Files\poppler-22.04.0\Library\bin')

#guradr y psar a formatao jpg
for pag in pdf_imagen:
    file_name=str(pdf.replace('.pdf', ''))+".jpg"
    pag.save(file_name,'JPEG')

#recortar 
read=cv2.imread(file_name)
new_image=str(pdf.replace('.pdf', ''))+" edit"+".jpg"
crop_img=read[540:2000, 250:4230]
cv2.imwrite(new_image, crop_img)
 
#extracion del text 
salida=str(pdf.replace('.pdf', ''))+".txt" 
#añadir a la salida
entorno = open(salida,"a")

text= Image.open(new_image)
resultado = pytesseract.image_to_string(text)

#guardar en txt
entorno.write(resultado)
entorno.close()

print('listo')
