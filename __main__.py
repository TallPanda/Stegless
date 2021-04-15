from stegless.magicnum import getmagic
from stegless.strings import strings
from stegless.tesseract import ocr
from stegless.bw import me as binwalk
from stegless.flagfinder import find
from sys import argv
from stegless.RGBvalues import RGBFull 
#from thirdparty.PCRT import pcrt as repair #third party png repair tool


def fstrings(_file,beginning="{",end="}"):#Full Strings #Basically strings with a for loop for mutiple outputs
    _ = find(strings(_file),beginning,end)
    if _ == []:
                print("Flag not found")
    else:
        for __ in _:
            print(f"Possiible flag: {__}")

def focr(_file):#Full OCR #basically just ocr with try excepts
    try:
            _ = ocr(_file)
            if not _ == None and not _ == "":
                return(f"Possible flags: {_}\nOCR finished")
            else:
                return("Nothing found")
    except Exception as e:
        return(f"{e}\nOCR Failed")

def binwalkies(_file, beginning="{",end="}"):# some cleaining up so main isnt stuffed
    for _ in binwalk(_file): #Looping through the output of files to preform further actions
        print(focr(_))
        try:
            fstrings(_,beginning,end)
            
        except Exception as e:
            print(f"{e}\n Flag not found")

def main(_file, beginning="{",end="}"):#Yes I know end,beginning are redundant but its safer that way
    print (getmagic(_file))
    fstrings(_file)
    print(focr(_file))
    binwalkies(_file, beginning,end)
    

if __name__ == "__main__":
    main(argv[1])
