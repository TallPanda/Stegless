from stegless.magicnum import getmagic
from stegless.strings import strings
from stegless.tesseract import ocr
from stegless.bw import me as binwalk
from sys import argv
def main(_file):
    print (getmagic(_file))
    print (strings(_file,"flag{","}"))
    print (ocr(_file))
    print (binwalk(_file))

if __name__ == "__main__":
    main(argv[1])