import re
def find(inp: list,start="{",end="}"):
    out = []
    for _ in inp:
        out.append(re.findall(f"{start}.*?{end}",_))
    return(out)