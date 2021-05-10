import re
def find(inp: list,start: str="{",end: str="}")-> list:
    """
    Takes in a list and returns a list begining with the given start variable and ending with the given end variable
    """
    assert(isinstance(inp,list)),f"input(AKA inp) not a list\nInput: {inp}\nType: {type(inp)}"
    if start and end:
        assert(isinstance(start,str) and isinstance(end,str)),f"Start or End not a string\nStart: {start}\nType: {type(start)}\nEnd: {end}\nType: {type(end)}"
    out = []
    for _ in inp:
        temp = re.findall(f"{start}.*?{end}",_)
        if temp:
            out.append(temp)
    return(out)