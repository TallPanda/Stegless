from stegless.magicnum import getmagic
from stegless.inhousestrings import strings
from stegless.tesseract import ocr,folderocr
from stegless.bw import binw
from stegless.flagfinder import find
from stegless.RGBvalues import pallet
import argh
#from thirdparty.PCRT import pcrt as repair #third party png repair tool


def fstrings(file,beginning="{",end="}"):#Full Strings #Basically strings with a for loop for mutiple outputs
    i = find([out for out in strings(file)],beginning,end)
    for ii in i:
        if ii == [] :
            pass
            # print("Flag not found")
        else:
            for iii in ii:
                print(f"Possiible flag: {iii}")

def focr(file):#Full OCR #basically just ocr with try excepts
    try:
            i = ocr(file)
            if not i == None and not i == "":
                return(f"Possible flags: {i_}\nOCR finished")
            else:
                return("Nothing found")
    except Exception as e:
        return(f"{e}\nOCR Failed")

def binwalkies(file, beginning="{",end="}"):# some cleaining up so main isnt stuffed
    for i in binw(file): #Looping through the output of files to preform further actions
        print(focr(i))
        try:
            fstrings(i,beginning,end)
            
        except Exception as e:
            print(f"{e}\n Flag not found")

def main(file, beginning="{",end="}"):
    "General scan Running binwalk, strings and returning metadata"
    print (getmagic(file))
    fstrings(file)
    print(focr(file))
    binwalkies(file, beginning,end)

parser = argh.ArghParser()
parser.add_commands([main,pallet,folderocr,ocr,getmagic])

if __name__ == "__main__":
    parser.dispatch()
