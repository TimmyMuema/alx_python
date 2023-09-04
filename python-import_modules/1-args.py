import sys

def print_arguments():
    """Prints the number of and the list of its arguments."""

    argc = len(sys.argv[1:])

    print("{} argument(s):\n".format(argc))
    if argc == 0:
        return

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
