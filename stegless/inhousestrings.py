import re
def strings(file):
    """
    creates an itterable containing all strings
    """
    assert(isinstance(file,str)),f"Path(AKA folder) not a string\nFolder: {file}\nType: {type(file)}"
    a = []
    with open(f"{file}", "rb") as f:
        _ = f.readable()
        line = -1
        while _:
            _line= line
            line = f.tell()
            if line ==_line:
                return range(1)
            s = f.readline()
            for num,stringz in enumerate([re.sub(r"[^\x20-\x7e\xa0-\xff]","",_) for _ in re.split("\s",s.decode("latin1"))]):
                if not stringz in a and len(stringz)>=4:
                    yield(stringz)
