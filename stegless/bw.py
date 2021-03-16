import binwalk
def me(_file):
    files =[]
    print("Beginning Binwalk Scan")
    for module in binwalk.scan(_file,signature=True,quiet=False, extract=True):
        for results in module.results:
            _files = module.extractor.output[results.file.path].extracted[list(module.extractor.output[results.file.path].extracted)[0]].files
            for f in _files:
                if not f in files:
                    files.append(f)
    print("Finished Binwalk Scan")
    return(files)