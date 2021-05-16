from subprocess import run

def steghide(file: str, password: str=''):
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nfile: {file}\nType: {type(file)}"
    assert(isinstance(password,str)),f"Path(AKA password) not a string\npassword: {password}\nType: {type(password)}"
    if file[0] =='-':
        raise(Exception("Cannot start file name with '-'"))
    return(str(run(['steghide', 'extract', '-sf', file, '-p', password], capture_output=True).stdout))
    
def openstego(file: str, password: str=''):
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nfile: {file}\nType: {type(file)}"
    assert(isinstance(password,str)),f"Path(AKA password) not a string\npassword: {password}\nType: {type(password)}"
    if password != '':
        return(str(run(['openstego', 'extract', '-sf', file, '-p', password], capture_output=True).stdout))
    else:
        return(str(run(['openstego', 'extract', '-sf', file], capture_output=True).stdout))