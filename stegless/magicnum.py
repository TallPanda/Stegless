import magic
def getmagic(file:str)->str:
    """
    Returns the metadata for a file
    """
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nfile: {file}\nType: {type(file)}"
    return (magic.from_file(file))#Simply pulling the magic number data from the file 