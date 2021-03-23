from subprocess import run
from sys import argv

def steghide(_file, password=''):
    run(['steghide', 'extract', '-sf', _file, '-p', password])
    
def openstego(_file, password=''):
    if password != '':
        run(['openstego', 'extract', '-sf', _file, '-p', password])
    else:
        run(['openstego', 'extract', '-sf', _file])

# steghide(argv[1])
# openstego(argv[1])