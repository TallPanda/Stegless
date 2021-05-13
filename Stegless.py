from stegless.magicnum import getmagic
from stegless.inhousestrings import strings
from stegless.tesseract import ocr,folderocr
from stegless.bw import me as binwalk
from stegless.flagfinder import find
from sys import argv
from stegless.RGBvalues import pallet
import argh
#from thirdparty.PCRT import pcrt as repair #third party png repair tool


def fstrings(file,beginning="{",end="}"):#Full Strings #Basically strings with a for loop for mutiple outputs
    _ = find([out for out in strings(file)],beginning,end)
    for __ in _:
        if __ == [] :
            pass
            # print("Flag not found")
        else:
            for ___ in __:
                print(f"Possiible flag: {___}")

def focr(file):#Full OCR #basically just ocr with try excepts
    try:
            _ = ocr(file)
            if not _ == None and not _ == "":
                return(f"Possible flags: {_}\nOCR finished")
            else:
                return("Nothing found")
    except Exception as e:
        return(f"{e}\nOCR Failed")

def binwalkies(file, beginning="{",end="}"):# some cleaining up so main isnt stuffed
    for _ in binwalk(file): #Looping through the output of files to preform further actions
        print(focr(_))
        try:
            fstrings(_,beginning,end)
            
        except Exception as e:
            print(f"{e}\n Flag not found")

def main(file, beginning="{",end="}"):#Yes I know end,beginning are redundant but its safer that way
    "General scan Running binwalk, strings and returning metadata"
    print (getmagic(file))
    fstrings(file)
    print(focr(file))
    binwalkies(file, beginning,end)

parser = argh.ArghParser()
parser.add_commands([main,pallet,folderocr,ocr,getmagic])

if __name__ == "__main__":
    parser.dispatch()
