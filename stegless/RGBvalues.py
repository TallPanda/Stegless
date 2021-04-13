import numpy
from PIL import Image
import os
import errno

def RGBFull(_file,output="./",i=None):
    with Image.open(_file) as a:
        try:
            os.makedirs(f'{output}SteglessImages')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        if a.mode == 'P':
            b = a.getpalette()
            arr = [0 for _ in range(len(b))]
            arrw = [255 for _ in range(len(b))]
        if i and a.mode == 'P':
            for _ in range(256):
                f = i*3
                E = 768 - f-(_*3)
                x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                if len(x)>768:
                    break
                a.putpalette(x)
                a.save(f"{output}SteglessImages/P{i}_{_}.png")
        elif a.mode =='P':
            for _ in range(256):
                for i in range( 256):
                    f = i*3
                    E = 768 - f-(_*3)
                    x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
                    if len(x)>768:
                        break
                    a.putpalette(x)
                    a.save(f"{output}SteglessImages/P{i}_{_}.png")
        elif a.mode =='RGBA':
            b= a.split()
            for i,_ in enumerate(b):
                _.save(f"{output}SteglessImages/RGBA{i}.png")
        else:
            return None