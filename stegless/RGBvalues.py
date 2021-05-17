from typing import Optional
from argh.decorators import arg
import numpy
from PIL import Image
import os
import errno
def pallet(file:str, output: str="./", bitplane: int=None, full: bool=None):
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nFile: {file}\nType: {type(file)}"
    assert(isinstance(output,str)),f"Path(AKA output) not a string\nOutput: {output}\nType: {type(output)}"
    if bitplane:
        try:
            bitplane = int(bitplane)
        except Exception as e:
            print(f"Bitplane not a int\nbitplane: {bitplane}\nType: {type(bitplane)}")
        assert(isinstance(bitplane,int)),f"Bitplane not a int\nbitplane: {bitplane}\nType: {type(bitplane)}"
        assert(bitplane<=255 and bitplane>=0),f"Bitplane: {bitplane} cannot be above 255 or bellow 0"
    """Bitplane is the bitplane to start from INT 0-255 inclusive
Full runs all bitplanes Bool True or False 
Only works if pngs mode is P simply runs the rbg planes if mode is rgba or rgb"""
    with Image.open(file) as a:
        for _ in ['Full','Advanced','Initial','RGBA']:
            try:
                os.makedirs(f'{output}SteglessImages/{_}')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        if a.mode == 'P':
            b = a.getpalette()
            arrw = [255 for _ in range(len(b))]
            arr = [0 for _ in range(len(b))]
            if bitplane: ### advanced
                print(f"Advanced scan beginning at {bitplane}")
                for _ in range(256):
                    f = bitplane*3
                    E = 768 - f-(_*3)
                    x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                    if len(x)>768:
                        break
                    a.putpalette(x)
                    a.save(f"{output}SteglessImages/Advanced/P{bitplane}_{_}.png")
            elif full:
                print("Full Scan")
                for _ in range(256):
                    for i in range( 256):
                        f = i*3
                        E = 768 - f-(_*3)
                        x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                        if len(x)>768:
                            break
                        a.putpalette(x)
                        a.save(f"{output}SteglessImages/Full/P{i}_{_}.png")
            else: ### initial run
                for i in range( 256):
                    f = i*3
                    E = 768 - f-3
                    x = list(arr[:f] +arrw[f:f+3] +arr[:E])
                    if len(x)>768:
                        break
                    a.putpalette(x)
                    a.save(f"{output}SteglessImages/Initial/P{i}.png")
        elif a.mode =='RGBA':
            print("Type RGBA")
            b= a.split()
            for i,_ in enumerate(b):
                _.save(f"{output}SteglessImages/RGBA/RGBA{i}.png")
        else:
            print("Type not P or RGBA")
            return None