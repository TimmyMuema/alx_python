import sys

def print_arguments():
    """Prints the number of and the list of its arguments."""

    argc = len(sys.argv) - 1
    i = 1

    print("{} argument(s):\n".format(argc))
    while i <= argc:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

if __name__ == "__main__":
    print_arguments()

