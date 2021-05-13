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
inp: find list

positional variables

file: me, strings, getmagic, pallet, steghide, openstego, ocr string
folder: folderocr string
inp: find list

variable type
string: 
    file:   me, string, getmagic, pallet, steghide, openstego, ocr
    folder: folderocr
    start,end: find, folderocr
list:
    inp: find
bool:
    no_out: ocr
    all: folderocr
    full: pallet
int:
    bitplane: pallet


testcases:
    string:
        Full hex range using latin charset generated with allhexlatin
        What we expect: All tests to error out stating file not found
        Findings: 
            All tests errored out with file not found except 2:
                folderocr: variable = "*" result: Folderocr ran with no issues searching the current directory 
                steghide: variable = "-" result: Steghide begins running and hangs indefinitly, fix added causing an exception to be raised for any file begining with "-"
    list:
        []
        ""
        [""]
        [,]
        []
        [[]]
        [None]
        [None,None]
        [{}]
        [[None]]
        ["aaaa{s}","}","{}","{"]
        allhexlatin()
    bool: for bools we will only test the no_output of ocr as folderocr, and pallet also only use the bool to trigger a if statement. This will be done due to time constraints.
        allhexlatin()
        None
        False
        True
        {}
        []
    int:
        range of -20,278
        expected:
            only values from the range 0-255 inclusive
"""
def allhexlatin()-> list:
    dictionary =[f"{_}" for _ in range(10)] + ["a","b","c","d","e","f"]
    temp = []
    for i in range(16):
        for ii in range(16):
            temp.append(bytes.fromhex(f"{dictionary[i]}{dictionary[ii]}").decode("latin1"))
    return temp

def stringstest(a):
    for s in a:
        #file
        try:
            me(s)
        except Exception as e:
            print(e,"\nme")
        try:
            strings(s)
        except Exception as e:
            print(e,"\nstrings")
        try:
            getmagic(s)
        except Exception as e:
            print(e,"\ngetmagic")
        try:
            pallet(s)
        except Exception as e:
            print(e,"\npallets")
        try:
            steghide(s)
        except Exception as e:
            print(e,"\nsteghide")
        try:
            openstego(s)
        except Exception as e:
            print(e,"\nopenstego")
        try:
            ocr(s)
        except Exception as e:
            print(e,"\nocrs")
            #folder
        try:
            folderocr(s)
        except Exception as e:
            print(e, "\nfolderocrs")

def listtest(a):
    listy =[
        [],
        "",
        [""],
        [],
        [[]],
        [None],
        [None,None],
        [{}],
        [[None]],
        ["aaaa{s}","}","{}","{"],
        a
    ]
    for l in listy:
        try:
            print(f"\n\nFound: {find(l)}")
            print(f"yeee\nList: {l}")
        except Exception as e:
            print(f"\n\n{e}",f"\nnooo\nlist: {l}")

def booltest(a):
    listy = [None, False, True, {}, [], [[]], [{}], '', ""]+ a
    for l in listy:
        try:
            print(ocr("testimages/strings-stego.jpg",l))
        except Exception as e:
            print(e)

def inttest():
    for i in range(-20,278):
        try:
            pallet("a",bitplane=i)
        except Exception as e:
            print(e,i)

def commands():
    cmdnames = ["me", "strings", "getmagic", "pallet", "steghide", "openstego", "ocr"]
    cmnds = [me, strings, getmagic, pallet, steghide, openstego, ocr]
    fakefiles = [f"testimages/a.{_}" for _ in ["jpg","png","gif"]]
    for name,cmd in zip(cmdnames,cmnds):
        for f in fakefiles:
            try:
                if cmd == strings:
                    print(f"\n\nRunning Strings on testimages/{f}")
                    for _ in strings(f):
                        print(_)
                else:
                    print(cmd(f))
                    print(f"{name} passed.\n")
            except Exception as e:
                print(f"{name} failed on {f} with:\n{e}\n\n")
        try:
            if cmd in [steghide,openstego]:
                print(cmd("testimages/strings-stego.jpg", password="password"))
                print(f"{name} passed.\n")
            elif cmd == strings:
                print("\n\nRunning Strings on testimages/strings-stego.jpg")
                for _ in strings("testimages/strings-stego.jpg"):
                    print(_)
            else:
                print(cmd("testimages/strings-stego.jpg"))
                print(f"{name} passed.\n")
        except Exception as e:
            print(f"{name} failed on testimages/strings-stego.jpg with:\n{e}\n\n")

if __name__ == "__main__":
    # a = allhexlatin()
    # stringstest(a)
    # listtest(a)
    # booltest(a)
    # inttest()
    commands()