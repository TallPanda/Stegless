import sys
from PIL import Image
import pytesseract
import re

def ocr(file_path):
    print("Beginning OCR Scan")
    image = Image.open(file_path)
    tes = re.sub("\s","",pytesseract.image_to_string(image))
    image.close()
    return(tes)
    


