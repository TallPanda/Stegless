import re
from sys import argv
def strings(f):
    with open(f, encoding="UTF-8") as a:
        print()
        b = []
        print(a.readline())
        """
        for _ in re.findall("\S+",a.read()):
            try:
                if not _ in b:
                    b.append(_)
            except Exception as e:
                print(e)
        """
    return(b)
[print(_) for _ in strings(argv[1])]