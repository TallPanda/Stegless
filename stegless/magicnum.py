import magic
def getmagic(file):
    return (magic.from_file(file))#Simply pulling the magic number data from the file 