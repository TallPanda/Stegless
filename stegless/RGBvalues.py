from typing import Optional
from argh.decorators import arg
import numpy
from PIL import Image
import os
import errno
def pallet(file:str, output: str="./", bitplane: int=None, full: bool=None):
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nFile: {file}\nType: {type(file)}"
    assert(isinstance(out,str)),f"Path(AKA out) not a string\nOut: {out}\nType: {type(out)}"
    """Bitplane is the bitplane to start from INT 0-256
Full runs all bitplanes Bool True or False 
Only works if pngs mode is P simply runs the rbg planes if mode is rgba or rgb"""
    with Image.open(file) as a:
        try:
            os.makedirs(f'{output}SteglessImages/Full')
            os.makedirs(f'{output}SteglessImages/Advanced')
            os.makedirs(f'{output}SteglessImages/Initial')
            os.makedirs(f'{output}SteglessImages/RGBA')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        if a.mode == 'P':
            b = a.getpalette()
            arrw = [255 for _ in range(len(b))]
            arr = [0 for _ in range(len(b))]
        if bitplane and a.mode == 'P': ### advanced
            print("Type P")
            for _ in range(256):
                f = bitplane*3
                E = 768 - f-(_*3)
                x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                if len(x)>768:
                    break
                a.putpalette(x)
                a.save(f"{output}SteglessImages/Advanced/P{bitplane}_{_}.png")
        elif a.mode =='P': ### initial run
            for i in range( 256):
                f = i*3
                E = 768 - f-3
                x = list(arr[:f] +arrw[f:f+3] +arr[:E])
                if len(x)>768:
                    break
                a.putpalette(x)
                a.save(f"{output}SteglessImages/Initial/P{i}.png")
        elif a.mode =='P' and full:
            print("Type P")
            for _ in range(256):
                for i in range( 256):
                    f = i*3
                    E = 768 - f-(_*3)
                    x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                    if len(x)>768:
                        break
                    a.putpalette(x)
                    a.save(f"{output}SteglessImages/Full/P{i}_{_}.png")
        elif a.mode =='RGBA':
            print("Type RGBA")
            b= a.split()
            for i,_ in enumerate(b):
                _.save(f"{output}SteglessImages/RGBA/RGBA{i}.png")
        else:
            print("Type not P or RGBA")
            return None