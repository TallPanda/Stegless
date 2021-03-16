import sys
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr(file_path):
    
    image = Image.open(file_path)
    print(pytesseract.image_to_string(image))


