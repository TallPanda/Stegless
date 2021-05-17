import binwalk
def binw(file:str)-> list:
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nFile: {file}\nType: {type(file)}"
    files =[]
    print("Beginning Binwalk Scan")
    for module in binwalk.scan(file,signature=True,quiet=False, extract=True):## returns 
        for results in module.results:
            temp = results.file.path
            if not temp in files:
                files.append(temp)
            # try:
            #     temp = module.extractor.output[results.file.path]## name of the result extracted-> dict
            #     file = temp.extracted.values()[0].files# list of files for result -- we expect only one file but could have changes depending on library code its not clearly doccument
            #     print(list(temp.extracted.values())[0].files) 
            #     files = temp.extracted[list(temp.extracted)[0]].files
            #     for f in files:# Is needed incase of issues upstream
            #         if not f in files:# Check to ensure file exists in dictionary
            #             files.append(f)
            # except Exception as e:
            #     print(e)
    print("Finished Binwalk Scan")
    return(files)