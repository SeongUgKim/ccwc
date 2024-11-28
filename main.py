from os import path, remove
from args_setup import args_setup
import sys

def main(args):
    if args.c:
        if args.c.name != "<stdin>":
            print(f"{count_bytes(args.c.name)} {path.basename(args.c.name)}")
        else:
            print(f"{count_bytes(args.c)}")
    elif args.l:
        if args.l.name != "<stdin>":
            print(f"{count_lines(args.l.name)} {path.basename(args.l.name)}")
        else:
            print(f"{count_lines(args.l)}")
    elif args.w:
        if args.w.name != "<stdin>":
            print(f"{count_lines(args.w.name)} {path.basename(args.w.name)}")
        else:
            print(f"{count_lines(args.w)}")
    elif args.m:
        if args.m.name != "<stdin>":
            print(f"{count_lines(args.m.name)} {path.basename(args.m.name)}")
        else:
            print(f"{count_lines(args.m)}")
    else:
        if args.input_file is not None:
            file = args.input_file
            print(
                f"{count_lines(file)}, {count_words(file)}, {count_bytes(file)}, {path.basename(file)}"
            )
        else:
            stdin_content = sys.stdin.read()
            file_name = "temp.txt"
            with open(file_name, "w") as file:
                file.write(stdin_content)
            print(
                f"{count_lines(file_name)}, {count_words(file_name)}, {count_bytes(file_name)}, {path.basename(file_name)}"
            )
            if path.exists(file_name):
                remove(file_name)
    pass
def count_bytes(file_name):
    try:
        if file_name is sys.stdin:
            # read from stdin -> could throw an OSError
            stdin_content = sys.stdin.read().encode("utf-8")
            bytes_size=len(bytes(stdin_content))
            return bytes_size
        else:
            try:
                # could throw a FileNotFoundError if file does not exist
                file_size = path.getsize(file_name)
                return file_size
            except FileNotFoundError:
                return f"File: {path.basename(file_name)} not found"
    except OSError:
        return "OS error occurred"
def count_lines(file_name):
    total_lines = 0
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")
            lines = stdin_content.splitlines()
            for line in lines:
                total_lines += 1
            return total_lines
        else:
            try:
                with open(file_name, "r") as file:
                    for line in file:
                        total_lines += 1
                return total_lines
            except FileNotFoundError:
                return f"File: {path.basename(file_name)} not found"
    except OSError:
        return "OS error occurred"
def count_words(file_name):
    total_words = 0
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")
            words = stdin_content.split()
            total_words += len(words)
            return total_words
        else:
            try:
                with open(file_name, "r") as file:
                    for line in file:
                        words = line.split()
                        total_words += len(words)
                return total_words
            except FileNotFoundError:
                return f"File: {path.basename(file_name)} not found"
    except OSError:
        return "OS error occured"
def count_characters(file_name):
    total_caracters = 0
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")
            for char in stdin_content:
                total_caracters +=1
            return total_caracters
        else:
            try:
                with open(file_name, "r") as file:
                    for line in file:
                        total_caracters += len(line.encode("utf-8"))
                return total_caracters
            except FileNotFoundError:
                return f"File: {path.basename(file_name)} not found"
    except OSError:
        return "OS error occurred"
    
if __name__ == "__main__":
    args = args_setup()
    main(args)