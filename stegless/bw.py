import binwalk
def me(_file):
    for module in binwalk.scan(_file,signature=True,quiet=False, extract=True):
        print ("%s Results:" % module.name)