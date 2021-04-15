import sys
from PIL import Image
import pytesseract
import re
import glob

def ocr(file_path, fleg=None):
    if not fleg:
        print(f"Beginning OCR Scan on {file_path}")
    image = Image.open(file_path)
    tes = re.sub("\s","",pytesseract.image_to_string(image))
    image.close()
    if not fleg:
        with open("tessoutput.txt", 'a') as f:
            f.write(f"\n{tes}       ::      {file_path}")
    return(tes)
    

def folderocr(folder):
    print(f"Beginning OCR Folder Scan on {folder}")
    for filepath in glob.iglob(f'{folder}/'+r'*.png'):
        try:
            a =ocr(filepath, "Yis")
            if any([_ in a for _ in ["{","}","ctf"] ]):
                with open("tessoutput.txt", 'a') as f:
                    f.write(f"\n{a}     ::      {filepath}")
        except Exception:
            print(f"OCR failed on {filepath}")
            pass