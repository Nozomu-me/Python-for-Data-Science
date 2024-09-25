import sys

argument = sys.argv[1]

try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert argument.isdigit(), "argument is not an integer"
except AssertionError as e:
    print(e)
    sys.exit(1)
if (int(argument) % 2) == 0:
    print("I'm Even.")
elif (int(argument) % 2) != 0:
    print("I'm Odd.")
