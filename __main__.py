from stegless.magicnum import getmagic
from stegless.strings import strings
def main():
    print (getmagic(__file__))
    print (strings("strings-stego.jpg","f","}"))

if __name__ == "__main__":
    main()