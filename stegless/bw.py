import binwalk
def binw(file:str)-> list:
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nFile: {file}\nType: {type(file)}"
    files =[]
    print("Beginning Binwalk Scan")
    for module in binwalk.scan(file,signature=True,quiet=False, extract=True):
        for results in module.results:
            try:
                files = module.extractor.output[results.file.path].extracted[list(module.extractor.output[results.file.path].extracted)[0]].files
                for f in files:
                    if not f in files:
                        files.append(f)
            except Exception as e:
                print(e)
    print("Finished Binwalk Scan")
    return(files)