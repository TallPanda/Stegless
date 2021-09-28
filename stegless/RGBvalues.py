from PIL import Image
import os
import errno
import random
from numpy.lib import save


def pstuff(img, output: str="./", bitplane: int=None, full: bool=None):
    if bitplane: ### advanced
        print("Type P")
        for _ in range(255):
            if _+bitplane >= 255:
                break
            colour = [random.randint(20,255), random.randint(20,255), random.randint(20,255)]
            x = [0 for i in range (bitplane*3)] + [c for i in range (_) for c in colour]+([0 for i in range (3*(255-bitplane-_))]) # randomly picks colours for second section to make it easier to differntiate between results
            if len(x)>768:
                print(len(x))
                break
            img.putpalette(x)
            img.save(f"{output}SteglessImages/Advanced/P{bitplane}_{_}.png")
    elif full:## same as advanced but brute forces every possible start point
        print("Type P")
        for _ in range(255):
            for bitplane in range( 256):
                if (_+ bitplane) >= 255:
                    break
                x = [0,0,0]*bitplane + ([random.randint(1,255) for i in range (3*_)])+([0,0,0]*(255-bitplane-_))
                if len(x)>768:
                    break
                img.putpalette(x)
                img.save(f"{output}SteglessImages/Full/P{bitplane}_{_}.png")
    else: ### Standard retrieval
        for i in range( 256):
            x = [0 for _ in range (i*3)]+[255,255,255]+[0 for _ in range (3*(255-i)) ]## 256 sets of three colours rgb filling all of them with a black except  the three at position i
            if len(x)>768:# Check to ensure it is the correct lenght or less
                break
            img.putpalette(x)
            img.save(f"{output}SteglessImages/Initial/P{i}.png")

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
Full runs all bitplanes Bool True or False"""
    with Image.open(file) as a:
        for name in ["Full","Advanced","Initial"]:
            try:## testing if direcories exist
                os.makedirs(f'{output}SteglessImages/{name}')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        if a.mode == 'P':
            pstuff(a, output,bitplane,full)
        
        else:# make image a type P image so we can apply pallets this replaces the spliting for colour channels in old method 
            z = a.quantize()
            pstuff(z, output,bitplane,full)