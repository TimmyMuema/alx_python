#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("Number of argument(s):")
        print(".")
    elif argc == 1:
        print("Number of argument(s) followed by argument:")
    else:
        print("Number of argument(s) followed by arguments:")

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()

