import re
def strings(_file):
    a = []
    with open(f"{_file}", "rb") as f:
        _ = f.readable()
        count = 0
        line = -1
        while _:
            _line= line
            line = f.tell()
            if line ==_line:
                return range(1)
            s = f.readline()
            for num,stringz in enumerate([re.sub(r"[^\x20-\x7e\xa0-\xff]","",_) for _ in re.split("\s",s.decode("latin1"))]):
                if not stringz in a and len(stringz)>=4:
                    # a.append(strings)
                    yield(stringz)
            count+=1
