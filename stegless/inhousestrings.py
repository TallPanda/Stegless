import re
def strings(file: str):
    """
    creates an itterable containing all strings
    """
    assert(isinstance(file,str)),f"Path(AKA folder) not a string\nFolder: {file}\nType: {type(file)}"
    a = []
    with open(f"{file}", "rb") as f:
        readable = f.readable()
        line = -1
        while readable:
            _line= line
            line = f.tell()
            if line ==_line:
                return range(1)
            s = f.readline()
            for stringz in [re.sub(r"[^\x20-\x7e\xa0-\xff]","",output) for output in re.split("\s",s.decode("latin1"))]:
                if not stringz in a and len(stringz)>=4:
                    with open(f"{file}-strings","a") as o:
                        o.write(f"{stringz}\n")
                    yield(stringz)
