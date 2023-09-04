import sys

def print_arguments():
    """Prints the number of command-line arguments and their values."""

    argc = len(sys.argv[1:])

    print("{} argument(s):\n".format(argc))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
