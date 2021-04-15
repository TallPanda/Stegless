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
    

def folderocr(folder: str,flegs: list=None,_all: str=None):
    print(f"Beginning OCR Folder Scan on {folder}")
    for filepath in glob.iglob(f'{folder}/'+r'*.png'):## :Looks for pngs
        try:
            a =ocr(filepath, "Yis")
            if _all:
                with open("tessoutput.txt", 'a') as f:
                    f.write(f"\n{a}     ::      {filepath}")
            elif any([_ in a for _ in [flegs]]):##or statement on a list
                with open("tessoutput.txt", 'a') as f:
                    f.write(f"\n{a}     ::      {filepath}")
        except Exception:
            print(f"OCR failed on {filepath}")
            pass