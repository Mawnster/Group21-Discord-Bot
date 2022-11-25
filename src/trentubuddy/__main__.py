import sys
from .trentubuddy import bot as trentubuddy

def main(args=None):
    trentubuddy.load_bot()

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do. Return values are exit codes.

if __name__ == "__main__":
    sys.exit(main())
