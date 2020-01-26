# Duplicate file finder main program

import argparse


def ParseArguments(args=None):
    parser = argparse.ArgumentParser(description='Duplicate file finder utility.')
    parser.add_argument('-v', dest='verbose', help='Verbose output', action='store_true')

    args = parser.parse_args(args=args)
    return args


if __name__ == "__main__":

    args = ParseArguments()
    if args.verbose:
        print('Searching for duplicate files...')
