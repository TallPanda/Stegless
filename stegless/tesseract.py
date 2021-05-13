from PIL import Image
import pytesseract
import re
import glob

def ocr(file:str, no_out: bool=None) -> str:
    assert(isinstance(file,str)),f"Path(AKA folder) not a string\nFolder: {file}\nType: {type(file)}"
    # if not fleg: I forgot why i had this so commeneted for now
    #     print(f"Beginning OCR Scan on {file}")
    image = Image.open(file)
    tes = re.sub("\s","",pytesseract.image_to_string(image))
    image.close()
    if not no_out:
        with open("tessoutput.txt", 'a') as f:
            f.write(f"\n{tes}       ::      {file}")
    return(tes)
    

def folderocr(folder: str,start: str="{", end: str="}", all: bool=None):
    assert(isinstance(folder,str)),f"Path(AKA folder) not a string\nFolder: {folder}\nType: {type(folder)}"
    if start and end:
        assert(isinstance(start,str) and isinstance(end,str)),f"Start or End not a string\nStart: {start}\nType: {type(start)}\nEnd: {end}\nType: {type(end)}"
    print(f"Beginning OCR Folder Scan on {folder}")
    ftypes= ["jpg","png", "jpeg", "png", "gif", "bmp", "tiff"]
    for ftype in ftypes:
        for file in glob.iglob(f'{folder}/'+f'*.{ftype}'):## :Looks for images
            try:
                a =ocr(file, "Yis")
                if all:
                    with open("tessoutput.txt", 'a') as f:
                        f.write(f"\n{a}     ::      {file}")
                else:
                    with open("tessoutput.txt", 'a') as f:
                        a = re.findall(f"{start}.*?{end}",a)
                        if a:
                            f.write(f"\n{a}     ::      {file}")
            except Exception as e:
                print(f"OCR failed on {file}\n{e}")