import binwalk
for module in binwalk.scan(__file__,signature=True,quiet=False, extract=True):
    print ("%s Results:" % module.name)