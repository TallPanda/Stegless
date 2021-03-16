import sys
from PIL import Image
import pytesseract

def ocr(file_path):
    
    image = Image.open(file_path)
    print(pytesseract.image_to_string(image))
    image.close()


