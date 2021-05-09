import re
def find(inp,flags,flage):
    out = []
    for _ in inp:
        out.append(re.findall(f"{flags}.*?{flage}",_))
    return(out)