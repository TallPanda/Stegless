from subprocess import run
def strings(_file):
    a = str(run(["strings",_file], capture_output=True).stdout) #We're using the subprocess module to run strings and capturing the output
    return(a)