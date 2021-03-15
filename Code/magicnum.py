import magic
def getmagic(_file):
    return (magic.from_file(_file))#Simply pulling the magic number data from the file 