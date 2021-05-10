from subprocess import run
from sys import argv

def steghide(file: str, password: str=''):
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nfile: {file}\nType: {type(file)}"
    assert(isinstance(password,str)),f"Path(AKA password) not a string\npassword: {password}\nType: {type(password)}"
    run(['steghide', 'extract', '-sf', file, '-p', password])
    
def openstego(file: str, password: str=''):
    assert(isinstance(file,str)),f"Path(AKA file) not a string\nfile: {file}\nType: {type(file)}"
    assert(isinstance(password,str)),f"Path(AKA password) not a string\npassword: {password}\nType: {type(password)}"
    if password != '':
        run(['openstego', 'extract', '-sf', file, '-p', password])
    else:
        run(['openstego', 'extract', '-sf', file])