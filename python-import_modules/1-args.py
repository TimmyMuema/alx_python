import sys

args = sys.argv[1:]

if not args:
    print("0 arguments.")
elif len(args) == 1:
    print("1 argument:")
    print(args[0])
else:
    print("{} arguments:".format(len(args)))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
