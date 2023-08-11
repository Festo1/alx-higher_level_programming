#!/usr/bin/python3

#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys


    count = len(sys.argv) -1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print ("{} arguments":)
    else:print("{} arguments:".format(cont))
    for a in range(count):
        print("{}: {}".format(a + 1, sys.argv[a +1]))
