import sys

def print_arguments():
    """Prints the number of and the list of its arguments."""

    argc = len(sys.argv) - 1

    print("{} argument(s):\n".format(argc))
    if argc == 0:
        return

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    print_arguments()
