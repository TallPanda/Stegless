#!/usr/bin/env python3
from stegless.magicnum import getmagic
from stegless.inhousestrings import strings
from stegless.flagfinder import find
from stegless.bw import me
from stegless.RGBvalues import pallet
from stegless.steg_tools import steghide,openstego
from stegless.tesseract import ocr,folderocr
"""
bw.py: me
flagfinder.py: find
inhousestrings.py: strings
magicnum.py: getmagic
RGBvalues.py: pallet
steg_tools.py: steghide openstego
tesseract.py: ocr folderocr
Variables
file:   me, string, getmagic, pallet, steghide, openstego, ocr string
folder: folderocr string
start,end: find, folderocr string
no_out: ocr bool
all: folderocr bool
bitplane: pallet int
full: pallet  bool

positional variables

file: me, strings, getmagic, pallet, steghide, openstego, ocr string
folder: folderocr string
inp: find string

variable type
string: 
    file:   me, string, getmagic, pallet, steghide, openstego, ocr
    folder: folderocr
    start,end: find, folderocr
    inp: find
bool:
    no_out: ocr
    all: folderocr
    full: pallet
int:
    bitplane: pallet


testcases:
    string:
        ""
        ""

"""
def allhexlatin()-> list:
    dictionary =[f"{_}" for _ in range(10)] + ["a","b","c","d","e","f"]
    temp = []
    for i in range(16):
        for ii in range(16):
            temp.append(bytes.fromhex(f"{dictionary[i]}{dictionary[ii]}").decode("latin1"))
    return temp

def stringstest():
    a = allhexlatin()
    for s in range(len(a)):
        for _s in range(len(a)):
            for _s_ in range(len(a)):
                try:
                    print(a[s]+a[_s]+a[_s_])
                except Exception as e:
                    print(e)
                    #file
                try:
                    me(s)
                except Exception as e:
                    print(e)
                try:
                    strings(s)
                except Exception as e:
                    print(e)
                try:
                    getmagic(s)
                except Exception as e:
                    print(e)
                try:
                    pallet(s)
                except Exception as e:
                    print(e)
                try:
                    steghide(s)
                except Exception as e:
                    print(e)
                try:
                    openstego(s)
                except Exception as e:
                    print(e)
                try:
                    ocr(s)
                except Exception as e:
                    print(e)
                    #folder
                try:
                    folderocr(s)
                except Exception as e:
                    print(e)
                    #inp
                try:
                    find(s)
                except Exception as e:
                    print(e)


if __name__ == "__main__":
    stringstest()