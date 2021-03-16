import re
def find(inp,flags,flage):
    return(re.findall(f"{flags}.*?{flage}",inp))