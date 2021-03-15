from subprocess import run
import re
def strings(_file,flagstart,flagend):
    a = str(run(["strings",_file], capture_output=True).stdout) #We're using the subprocess module to run strings and capturing the output
    return(re.findall(f"{flagstart}.*?{flagend}",a)) #regex to search for everything matching our flag format