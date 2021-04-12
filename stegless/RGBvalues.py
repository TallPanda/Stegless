import numpy
# import re
# a = open("sunrise.png","rb")
# print(re.findall(b".*IHDR.*",a.read()))
# a.close()
from PIL import Image
a = Image.open("testimages/doge_stege.png")
#a.equalize().show()
b = a.getpalette()
arr = [0 for _ in range(len(b))]
arrw = [255 for _ in range(len(b))]
print(len(b))
# for i in range(256):
#     x = list(arr[0:i*3] +b[i*3:i*3+2] + arr[i*3+2:])
#     a.putpalette(x)
#     a.save(f"testimages/{i}.png")

for _ in range(256):
    for i in range( 256):
        i = 127
        f = i*3
        E = 768 - f-(_*3)
        x = list(arr[:f] +arrw[f:f+(_*3)] +arr[:E])
        if len(x)>768:
            break
        a.putpalette(x)
        a.save(f"testimages/splitpics/{i}_{_}.png")

# b = numpy.array([b[]for i in 256])
# a.putpalette(list(b))
# a.show()
# b = a.split()
# print(b)
# for i,_ in enumerate(b):
#     _.save(f"testimages/{i}.png")
# for i in "rgba":
#     a.convert(mode=i).save(f"testimages/{i}.png")