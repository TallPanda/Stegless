from subprocess import run
from sys import argv
import re
f=argv[1]
flagstart=argv[2]
flagend=argv[3]
a = str(run(["strings",f], capture_output=True).stdout)
print(re.findall(f"{flagstart}.*?{flagend}",a))