import binwalk
def me(file:str)-> list:
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nFile: {file}\nType: {type(file)}"
    files =[]
    print("Beginning Binwalk Scan")
    for module in binwalk.scan(file,signature=True,quiet=False, extract=True):
        for results in module.results:
            files = module.extractor.output[results.file.path].extracted[list(module.extractor.output[results.file.path].extracted)[0]].files
            for f in files:
                if not f in files:
                    files.append(f)
    print("Finished Binwalk Scan")
    return(files)