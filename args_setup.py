import argparse
import sys

def args_setup():
    parser = argparse.ArgumentParser(
        description="ccwc - word, line, character, and byte count"
    )
    parser.add_argument(
        "-c",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of bytes in each input file is written to the sgtandard output",
    )
    parser.add_argument(
        "-l",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of lines in each input file is written to the sgtandard output",
    )
    parser.add_argument(
        "-w",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of words in each input file is written to the sgtandard output",
    )
    parser.add_argument(
        "-m",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of characters in each input file is written to the sgtandard output",
    )
    parser.add_argument(
        "input_file", 
        nargs="?",
        help="A positional argument which can take a file name or standard input when no flag is given",
    )
    args = parser.parse_args()
    return args