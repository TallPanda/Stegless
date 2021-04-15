import numpy
from PIL import Image
import os
import errno

def RGBFull(_file,output="./",i=None,full=None):
    with Image.open(_file) as a:
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
        if i and a.mode == 'P': ### advanced
            print("Type P")
            for _ in range(256):
                f = i*3
                E = 768 - f-(_*3)
                x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                if len(x)>768:
                    break
                a.putpalette(x)
                a.save(f"{output}SteglessImages/Advanced/P{i}_{_}.png")
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